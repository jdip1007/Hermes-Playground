---
title: Hermes Proxy (OAuth → OpenAI compatible local proxy)
created: 2026-05-22
updated: '2026-06-08'
type: concept
tags:
- agent-system
- oauth
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Hermes Proxy

## Overview

`hermes proxy` Expose OAuth subscriptions (Nous Portal, xAI SuperGrok, and future extensions Claude Pro / ChatGPT Pro) as OpenAI-compatible native HTTP endpoints. Any client that recognizes the OpenAI API (Codex CLI, Aider, Cline, Continue, and your own script) can connect directly without an API key and reuse your existing subscriptions.[1][1]

v0.14 landed (PR `#25969`). The code is in `hermes_cli/proxy/` 。[1]

### design principles

> The proxy is intentionally minimal. It does NOT mediate, log, transform, or rewrite request/response bodies—it's a credential-attaching forwarder.
> —— `hermes_cli/proxy/server.py:1-10`

Strip the client Authorization header → Inject the upstream OAuth bearer → Transparently transmit SSE/JSON as it is. No prompt overwriting, accounting interception or logging.[1]

---

## start up

```bash
hermes proxy start [--provider nous|xai] [--host 127.0.0.1] [--port 8645]
```

| parameter | default | illustrate |
|------|------|------|
| `--provider` | `nous` | upstream adapter name |
| `--host` | `127.0.0.1` | bind address,`0.0.0.0` Open LAN |
| `--port` | `8645` | port |

Entrance:`hermes_cli/proxy/cli.py:30-75` `cmd_proxy_start()`：

1. Check if aiohttp is available (line 35), if missing, prompt `hermes-agent[messaging]`
2. Resolve adapter by provider name (line 41)
3. Verify logged in `adapter.is_authenticated()`（line 46）
4. `asyncio.run(run_server(adapter, host=host, port=port))`（line 69）

Server starts:`server.py:255-300` `run_server()` Start aiohttp TCP site + signal handler.

### Status view

```bash
hermes proxy status
hermes proxy providers   # 或 proxy list
```

`status` Output adapter readiness + token expiration time.[1]

---

## Adapter abstract

### `UpstreamCredential`（`adapters/base.py:21-36`）

```python
@dataclass(frozen=True)
class UpstreamCredential:
    bearer: str                  # token 本体，无 "Bearer " 前缀
    base_url: str                # 如 https://inference-api.nousresearch.com/v1
    token_type: str = "Bearer"
    expires_at: Optional[str] = None
```

### `UpstreamAdapter` ABC（`adapters/base.py:38-107`）

| method | use |
|------|------|
| `name` (property) | provider key, such as `"nous"` |
| `display_name` (property) | Log name |
| `allowed_paths` (property) | `FrozenSet[str]` whitelist path |
| `is_authenticated()` | Fast non-blocking check |
| `get_credential()` | Return fresh bearer + base_url (refresh if necessary) |
| `get_retry_credential()` | Give alternative credentials after upstream 401 (optional) |

### Registry（`adapters/__init__.py:16-19`）

```python
ADAPTERS: Dict[str, Type[UpstreamAdapter]] = {
    "nous": NousPortalAdapter,
    "xai": XAIGrokAdapter,
}
```

`get_adapter(name) → UpstreamAdapter` The factory is on line 22.

---

## Supported Providers

### Nous Portal（`nous`）

`NousPortalAdapter` Class in `adapters/nous_portal.py:50`，`allowed_paths` property on line 67 returns module-level `_ALLOWED_PATHS`（line 40-47） 。[1]

**Whitelist**:
```python
{"/chat/completions", "/completions", "/embeddings", "/models"}
```

**OAuth integration**:[1]

- read `~/.hermes/auth.json` state
- tune `resolve_nous_runtime_credentials()` Refresh access token + get/exchange `agent_key`
- Dual mode: auto + legacy session key; automatically retry with legacy bearer when 401 occurs
- base URL：`DEFAULT_NOUS_INFERENCE_URL`(typical `https://inference-api.nousresearch.com/v1`，line 140）

### xAI Grok OAuth（`xai`） [1]

`XAIGrokAdapter` Class in `adapters/xai.py:31`，`allowed_paths` property on line 49 returns module-level `_ALLOWED_PATHS`（line 20-28）。

**Whitelist**:
```python
{"/responses", "/chat/completions", "/completions", "/embeddings", "/models"}
```
More than Nous `/responses` endpoint.

**OAuth integration**:

- `CredentialPool` credential pool (`load_pool("xai-oauth")`，line 104）
- `pool.select()` Choose one of the available credentials (line 65)
- 401: refresh first, if failed, mark exhausted and rotate (line 90-92)

**base URL**: The credential entry's `runtime_base_url` or `base_url`,default `DEFAULT_XAI_OAUTH_BASE_URL`（line 122-127）

**Auth Tips**:`"hermes auth add xai-oauth --type oauth"`（line 34）

---

## route shape [1]

All requests hang on `/v1/<path>`：

```python
app.router.add_route("*", "/v1/{tail:.*}", handle_proxy)
```
Location:`server.py:250`

For example nous adapter in `127.0.0.1:8645`：

- `POST /v1/chat/completions`
- `POST /v1/completions`
- `POST /v1/embeddings`
- `GET /v1/models`

Health check (no forwarding):

- `GET /health` → JSON status + upstream name (line 99-106)

**Path verification**:`rel_path not in adapter.allowed_paths` → Return to 404 `path_not_allowed`（line 124-131）

---

## Request forwarding [1]

`handle_proxy()` exist `server.py:119-246`：

1. Extract relative path
2. Verify path whitelist
3. `adapter.get_credential()` get bearer + base_url; failed → 401 `upstream_auth_failed`（line 134-137）
4. Read body into memory (line 143)
5. **Filter hop-by-hop header** (line 153), see below
6. injection `Authorization: Bearer <cred.bearer>`（line 154）
7. Pin upstream URL:`<base_url><rel_path>?<query_string>`（line 148-151）
8. aiohttp sends: connect timeout 15s, read timeout 300s (line 145)

### Hop-by-hop header filtering (`server.py:36-50`)

```python
_HOP_BY_HOP_HEADERS = frozenset({
    "host", "content-length", "connection", "keep-alive",
    "proxy-authenticate", "proxy-authorization", "te", "trailers",
    "transfer-encoding", "upgrade", "authorization",
})
```

The request header is filtered on line 153; the response header is filtered on line 230 (Content-Encoding / Content-Length is retained, recalculated by aiohttp).

### 401 Retry (`server.py:209-225`)

Upstream return 401:

1. `adapter.get_retry_credential(failed_credential=cred, status_code=401)`
2. Nous: Retry with legacy session key when JWT fails
3. xAI: pool refresh, if failed, rotate to the next available credential
4. Get new credentials → Resend request

---

## Streaming response [1]

Reprinted exactly as is:

1. rise `web.StreamResponse`, inherit the upstream status + filtered headers (line 228-231)
2. `async for chunk in upstream_resp.content.iter_any():` chunked read (line 235)
3. Write directly back to client (line 237)
4. SSE frames are preserved verbatim:

```
data: {"choices":[{"delta":{"content":"Hello"}}]}

data: {"choices":[{"delta":{"content":" world"}}]}

data: [DONE]
```

---

## Error response [1]

OpenAI style JSON (`_json_error()` line 56）：

```json
{
  "error": {
    "message": "...",
    "type": "code_string",
    "code": "code_string"
  }
}
```

| code | HTTP | trigger |
|------|------|------|
| `upstream_auth_failed` | 401 | adapter cannot get credentials |
| `path_not_allowed` | 404 | Path is not in allowed_paths |
| `upstream_unreachable` | 502 | Can't connect to upstream |
| `upstream_timeout` | 504 | upstream timeout |

---

## Concurrency safety [1]

Use thread lock inside the adapter to serialize credential parsing:

- `NousPortalAdapter._lock` exist `_get_credential()`（line 102）
- `XAIGrokAdapter._lock` exist `get_credential()`（line 57）

Cross-process token refresh and persistence are responsible for the respective auth subsystems (Nous shared runtime resolver, xAI credential pool).

---

## Client configuration example [1]

Any OpenAI compatible client:

```bash
export OPENAI_API_KEY=any-string-ignored
export OPENAI_BASE_URL=http://127.0.0.1:8645/v1
```

Then `aider --model claude-opus-4-7`、`cline`、`codex` When used directly, the credential is injected by proxy.

---

## File index [1]

| Function | File: line |
|------|-----------|
| Module docstring + export | `__init__.py:1-21` |
| CLI `proxy start` | `cli.py:30` |
| CLI `proxy status` | `cli.py:78` |
| `create_app()` aiohttp factory | `server.py:85` |
| `handle_proxy()` | `server.py:119` |
| `_filter_request_headers` / `_filter_response_headers` | `server.py:62` / `:72` |
| `UpstreamCredential` | `adapters/base.py:21` |
| `UpstreamAdapter` ABC | `adapters/base.py:38` |
| Registry + `get_adapter()` | `adapters/__init__.py:16` |
| `NousPortalAdapter` kind | `adapters/nous_portal.py:50` |
| `_ALLOWED_PATHS` (Nous) | `adapters/nous_portal.py:40` |
| `XAIGrokAdapter` kind | `adapters/xai.py:31` |
| `_ALLOWED_PATHS` (xAI) | `adapters/xai.py:20` |

> Module-level constants: `hermes_cli/goals.py` 762 lines, `kanban_db.py` 6286 lines, `agent/curator.py` 1781 lines, `proxy/server.py` 308 lines, `proxy/adapters/base.py` 109 lines (as of HEAD `09afafb87`）。

---

## Things not to do [1]

- Do not cache
- Do not log request body
- Do not change prompt / tools
- No billing
- No current limit (except upstream itself)
- No token translation

Any of the above requirements should be addressed to the upper layer, or a dedicated LLM gateway product (such as LiteLLM) should be used. The purpose of Hermes proxy is to "disguise" OAuth subscriptions as API keys, nothing more.

---

*Last verified: 2026-05-22, HEAD `09afafb87`*

## Related Pages

- [[Provider Transport Architecture|provider-transport-architecture]]
- [[Smart Model Routing|smart-model-routing]]
---
