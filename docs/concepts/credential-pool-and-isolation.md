

---
title: Credential pool and environment isolation system
created: 2026-04-07
updated: '2026-06-08'
type: concept
tags:
- agent-system
- security
- isolation
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Credential pool and environment isolation system

## Design principles

Enterprise scenarios require multiple API key implementations: [1]
1. **Load Balancing** — Multiple key sharing requests
2. **Failover** — Automatically switches when a key is rate-limited
3. **Cost Control** — Different keys have different budgets

Hermes implements a credential pool system that supports automatic rotation of multiple keys. [1]

## Credential pool architecture

The core data structure is located in `agent/credential_pool.py` (not `tools/`): [1]

- **`PooledCredential`** — A single credential entry (dataclass) containing `runtime_api_key`, `runtime_base_url`, depletion status, and count
- **`CredentialPool`** — Credential pool, manages the selection, rotation and recovery of multiple credentials

### 4 pool selection strategies

```yaml
# config.yaml
credential_pool:
  strategy: round_robin  # default
```

| Strategy | Behavior |
|------|------|
| `fill_first` | Keep using the first one until it runs out before cutting off the next one |
| `round_robin` | Rotate in turn and share evenly |
| `random` | Randomly select an available |
| `least_used` | Choose the least used |

### Key method[1]

- `select()` — Selects the next available credential by policy
- `mark_exhausted(entry)` — Tag exhaustion + automatic rotation (exhaustion TTL is 1 hour, automatic recovery after expiration)
- `try_refresh(entry)` — OAuth token refresh
- `has_available()` — whether there are any credentials available

## Voucher rotation logic[1]

```python
# 402 (billing exhausted) — rotate immediately
if status_code == 402:
    next_entry = pool.mark_exhausted_and_rotate(status_code=402, ...)
    if next_entry:
        self._swap_credential(next_entry)
        return True, False

# 429 (rate limit) — retry first time, rotate second time
if status_code == 429:
    if not has_retried_429:
        return False, True  # retry with same credential
    next_entry = pool.mark_exhausted_and_rotate(status_code=429, ...)
    if next_entry:
        self._swap_credential(next_entry)
        return True, False

# 401 (unauthorized) — refresh first, rotate on failure
if status_code == 401:
    refreshed = pool.try_refresh_current()
    if refreshed:
        self._swap_credential(refreshed)
        return True, has_retried_429
    # refresh failed — rotate
    next_entry = pool.mark_exhausted_and_rotate(status_code=401, ...)
    if next_entry:
        self._swap_credential(next_entry)
        return True, False
```

## Credential Exchange[1]

```python
def _swap_credential(self, entry) -> None:
    """Swap credential"""
    runtime_key = getattr(entry, "runtime_api_key", None)
    runtime_base = getattr(entry, "runtime_base_url", None) or self.base_url
    
    if self.api_mode == "anthropic_messages":
        self._anthropic_client.close()
        self._anthropic_api_key = runtime_key
        self._anthropic_base_url = runtime_base
        self._anthropic_client = build_anthropic_client(runtime_key, runtime_base)
        self._is_anthropic_oauth = _is_oauth_token(runtime_key)
        self.api_key = runtime_key
        self.base_url = runtime_base
        return
    
    # OpenAI 兼容模式
    self.api_key = runtime_key
    self.base_url = runtime_base.rstrip("/")
    self._client_kwargs["api_key"] = self.api_key
    self._client_kwargs["base_url"] = self.base_url
    self._replace_primary_openai_client(reason="credential_rotation")
```

## OAuth dead token quarantine(quarantine)[1]

MiniMax/Codex/xAI OAuth now isolates dead tokens on **terminating refresh failure**: when a refresh triggers `AuthError` (`relogin_required`) that requires a re-login, `access_token`, `refresh_token`, `expires_at` are stripped from `auth.json` and a `last_auth_error` record is written. In this way, subsequent calls will fail quickly and no network retries will be initiated (`hermes_cli/auth.py:6795-6811`, continuing the existing Nous isolation mode).

## Nous Invoke JWT takes precedence [1]

Nous inference authentication now prefers to use a **scope-restricted invoke JWT** (`invoke_jwt` in `auth.json`), directly as the `access_token` for inference. Fallback to the old opaque 24-hour session key (`hermes_cli/auth.py:16-17,89-94`) when JWT authentication is unavailable or fails. Setting `HERMES_AGENT_USE_LEGACY_SESSION_KEYS` forces the use of the old path for debugging or rollback.

## Environmental isolation[1]

```python
# HERMES_HOME isolation
def get_hermes_home() -> Path:
    """Get Hermes home directory (supports Profile override)"""
    env_override = os.getenv("HERMES_HOME")
    if env_override:
        return Path(env_override)
    return Path.home() / ".hermes"

# Profile support
# ~/.hermes/ is the default Profile
# HERMES_HOME=/path/to/custom uses custom Profile
```

### Profile isolated content[1]

| content | isolation | shared |
|------|------|------|
| Configuration (config.yaml) | ✅ | ❌ |
| Key (.env) | ✅ | ❌ |
| Skills (~/.hermes/skills/) | ✅ | ❌ |
| Memories (~/.hermes/memories/) | ✅ | ❌ |
| session database | ✅ | ❌ |
| code repository | ❌ | ✅ |

## Terminal backend environment isolation[1]

```python
# tools/environments/
# Each terminal backend provides an isolated execution environment

local.py      # local execution (shared filesystem)
docker.py     # Docker container isolation
ssh.py        # SSH remote execution
modal.py      # Modal serverless isolation
daytona.py    # Daytona sandbox isolation
singularity.py # Singularity container isolation
```

## Superiority Analysis[1]

### Comparison with other Agent frameworks

| characteristic | Hermes | Cursor | OpenCode |
|------|--------|--------|----------|
| Credential pool | ✅Multiple key rotation | ❌ | ❌ |
| Automatic failover | ✅ 402/429/401 | ❌ | ❌ |
| OAuth refresh | ✅ Automatic | ❌ | ❌ |
| Profile isolation | ✅ HERMES_HOME | ❌ | ❌ |
| Terminal backend isolation | ✅ 6 backends | ❌ | ✅ Docker |

## Related pages
- [[Multi Agent Architecture|multi-agent-architecture]]
- [[Agent Loop And Prompt Assembly|agent-loop-and-prompt-assembly]]

- [Interrupt And Fault Tolerance](interrupt-and-fault-tolerance.md) — Interrupt propagation and fault tolerance mechanism (credential rotation logic)
- [Auxiliary Client Architecture](auxiliary-client-architecture.md) — A secondary client obtains authentication using a credential pool
- [Configuration And Profiles](configuration-and-profiles.md) — Profile isolation and credential management

## Related documents

- `agent/credential_pool.py` — Credential Pool (4 strategies + exhaustion recovery)
- `hermes_cli/auth.py` — Credential parsing, OAuth dead token isolation, Nous invoke JWT
- `tools/environments/` — terminal backend environment