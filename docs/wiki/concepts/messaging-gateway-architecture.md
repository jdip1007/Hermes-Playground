---
title: Messaging Gateway Architecture
created: 2026-04-07
updated: '2026-06-08'
type: concept
tags:
- agent-system
- agent-pattern
- gateway
- ai-ml
sources:
- title: Hermes-Wiki Repository
  type: web
  url: https://github.com/cclank/Hermes-Wiki
confidence: high
contested: false
---
# Message gateway architecture

## Overview

Gateway is the **Unified Messaging Gateway** of Hermes Agent. As of 2026-05-24, it supports **23 messaging platforms** (including 6 plug-in platforms: IRC / Teams / Google Chat / LINE / SimpleX Chat / **ntfy**), managing connections and message distribution for all platforms from a single process [1].

## Architecture

```
gateway/
├── run.py              # 主循环、斜杠命令、消息分发
├── session.py          # SessionStore — 对话持久化
├── delivery.py         # 消息投递
├── config.py           # 网关配置
├── hooks.py            # 钩子系统
├── pairing.py          # DM 配对
├── status.py           # 状态管理
├── mirror.py           # 跨平台镜像
├── sticker_cache.py    # 贴纸缓存
├── stream_consumer.py  # 流式消费
├── channel_directory.py # 频道目录
├── platform_registry.py # 平台插件注册表（PlatformRegistry）
├── slash_access.py     # 按平台的 admin/user 斜杠命令分级
├── shutdown_forensics.py # 关停诊断/取证记录
└── platforms/          # 平台适配器
    ├── telegram.py
    ├── telegram_network.py
    ├── discord.py
    ├── slack.py
    ├── whatsapp.py
    ├── signal.py
    ├── email.py
    ├── sms.py
    ├── matrix.py
    ├── mattermost.py
    ├── dingtalk.py
    ├── feishu.py
    ├── wecom.py
    ├── weixin.py
    ├── bluebubbles.py
    ├── homeassistant.py
    ├── webhook.py
    ├── msgraph_webhook.py
    ├── api_server.py
    ├── msgraph_webhook.py   # MS Graph webhook（v0.13.x+）
    ├── yuanbao.py / _media / _proto / _sticker
    └── base.py

plugins/platforms/         # 插件化平台（v0.13.x+）
├── irc/                   # IRC（参考实现）
├── line/                  # LINE Messaging API
├── google_chat/           # Google Chat
├── teams/                 # Microsoft Teams
└── simplex/               # SimpleX Chat
```

## Platform support

### Built-in messaging platform (gateway/platforms/)[1]

The `Platform` Enum of source code `gateway/config.py:82-111` explicitly lists all built-in members. The following table removes `LOCAL` / `WEBHOOK` / `API_SERVER` / `MSGRAPH_WEBHOOK` / `WECOM_CALLBACK` these non-user dialogue platforms, leaving **17**[1]:

| platform | type | characteristic |
|------|------|------|
| Telegram | Bot API | Group/private chat, voice transcription, stickers, proxy support, link preview control, `allowed_chats` |
| Discord | Bot API | Server/private chat, voice channel, Slash Commands, `DISCORD_ALLOWED_ROLES` (guild-scoped from v0.13, blocking CVSS 8.1 cross-guild DM bypass), channel_prompts |
| Slack | Bot API | Workspace integration, Thread support, `strict_mention`, `channel_skill_bindings`, `allowed_channels` |
| WhatsApp | Bridge (Node.js) | Group/private chat, allow list, default **deny strangers** from v0.13 + never reply in self-chat |
| Signal | Bot API | Encrypted messages, native formatting, reply quotes, reactions (v2026.4.23+) |
| Email | IMAP/SMTP | Email interaction |
| SMS | Twilio | SMS, character limit |
| Home Assistant | WebSocket | smart home events |
| Matrix | E2E encryption | Decentralized messaging, `allowed_rooms` |
| Mattermost | Bot API | Self-hosted team messages, `allowed_channels` |
| DingTalk | Stream | Corporate news, QR code scanning authentication, require_mention + allowed_users permission control |
| Feishu/Lark | Stream | Enterprise messaging, `require_mention`, operational configurable bot admission policy (v0.13) |
| Enterprise WeChat | Stream | Enterprise WeChat messaging, QR code scanning bot creation (v2026.4.18+) |
| BlueBubbles | REST + Webhook | iMessage (macOS), tapback, read receipts |
| WeChat/WeChat | iLink Bot API | Long polling to receive messages, AES-128-ECB media encryption, QR login |
| QQ Bot | Official API v2 | WebSocket inbound (C2C/group/channel/DM) + REST outbound, voice transcription (Tencent ASR), allowlist + DM pairing |
| Webhook | HTTP | External event reception |
| **Tencent Yuanbao** | API | Native text + media delivery, sticker support (v2026.4.23+) |
| **IRC** (plugin) | TLS asyncio | Zero external dependencies, TLS, PING/PONG, nick collision, NickServ, channel addressing (v2026.4.23+, reference implementation) |
| **Microsoft Teams** (plug-in) | Graph + Webhook | v0.12 landing plug-in → v0.14 end-to-end: auth + webhook listener + pipeline + delivery (`plugins/teams_pipeline/`) |
| **Google Chat** (plug-in) | API | Platform 20 (v0.13, `plugins/platforms/google_chat/`) |
| **LINE** (plug-in) | Messaging API | Mainstream communications from Japan, Korea and Taiwan (v0.14, `plugins/platforms/line/`) |
| **SimpleX Chat** (plug-in) | Decentralized without ID | privacy-focused（v0.14，`plugins/platforms/simplex/`） |
| **Google Meet**（plugin） | OpenAI Realtime + Node bot | Meeting Access: Transcription + Follow-up (v0.12, `plugins/google_meet/`) |
| **ntfy** (plugin) | HTTP streaming sub + POST publish | Platform 23. `plugins/platforms/ntfy/`, zero additional dependencies (only httpx), no native user identity - each topic is treated as a single trusted channel (2026-05-23) |

> After being restored to a plug-in, the gateway core converged from 21 if/elif to 1 registry query; the new platform 0 code was changed to core[1].

## v0.13+ enhanced summary[1]

| Enhance | illustrate |
|------|------|
| **Session auto-resume** | Automatically resume unfinished sessions after the gateway restarts (`#21192`) |
| **Unified allowlist** | Slack/Telegram/Mattermost/Matrix/DingTalk all support `allowed_channels`/`allowed_chats`/`allowed_rooms` (`#21251`) |
| **WhatsApp Default rejection** | Default reject strangers (v0.13 safe wave) |
| **Discord History Backfill** | Entering the channel/thread for the first time to read the message history (`#25984`) |
| **Discord role-allowlist guild-scoped** | Fix CVSS 8.1 cross-guild DM bypass |
| **Native multi-image delivery** | Telegram/Discord/Slack/Mattermost/Email/Signal All affordable (`#17909`) |
| **FLAC Audio Routing** | + Telegram documentation fallback (`#17833`) |
| **`/handoff` real-time cut model/persona/profile** | Do not lose any message/tool ​​call (`#23395`) |
| **`clarify` native button** | Telegram + Discord multi-select platform button (`#24199/#25485`) |
| **Telegram skip-STT audio path + 2GB cap** | Via local Bot API server |
| **`ignore_root_dm` + lobby** | Telegram system command set (`c931dad1d`) |
| **`disable_topic_auto_rename`** | Telegram |
| **`pin incoming user message`** | Telegram |
| **`require_mention`** | Signal group chat only replies @ |
| **QQBot native approval keyboard** | Aligned with Telegram/Discord UX (`#21342/#21353`) |
| **Deliverable mode** | Any surface can ship native artifacts (`#27813`) |
| **i18n** | 7 locales: zh / ja / de / es / fr / uk / tr |

### Bundled platform plug-ins (plugins/platforms/)[1]

`gateway/platform_registry.py` introduces `PlatformRegistry` singleton + `PlatformEntry` dataclass, allowing anyone to access the new platform as a **pure plug-in** without changing the gateway core code [1].

There are currently 5 plug-in platforms under `plugins/platforms/`: `irc`, `line`, `google_chat`, `simplex`, `teams`. They are self-registered via `ctx.register_platform()` and automatically discovered by file system scan at startup (`Platform._missing_()` creates identity-stable pseudo-members for bundled plugins) [1].

```python
# 插件注册入口（hermes_cli/plugins.py 提供 ctx.register_platform）
def register(ctx):
    ctx.register_platform(
        name="line",
        label="LINE",
        adapter_factory=create_line_adapter,
        check_fn=check_line_available,
        validate_config=validate_line_config,
        required_env=["LINE_CHANNEL_ACCESS_TOKEN", "LINE_CHANNEL_SECRET"],
        install_hint="pip install line-bot-sdk",
    )
```

### `PlatformEntry` metadata field (gateway/platform_registry.py:37-143)

| Field | effect |
|------|------|
| `adapter_factory` / `check_fn` / `validate_config` / `is_connected` | Factory + Health Check |
| `required_env` / `install_hint` / `setup_fn` | Installation/configuration assistance |
| `allowed_users_env` / `allow_all_env` | `_is_user_authorized` Integration |
| `max_message_length` / `pii_safe` / `emoji` | Display/Privacy/Smart Sharding |
| `allow_update_command` | Whether the platform is allowed to trigger `/update` |
| `platform_hint` | Platform behavior prompts injected into the system prompt |
| `env_enablement_fn` ⭐ | Read from env vars, return dict (v0.13) to be seeded to `PlatformConfig.extra` |
| `cron_deliver_env_var` ⭐ | `*_HOME_CHANNEL` env name; let `cron.scheduler` recognize `deliver=<name>` as a legal target (v0.13) |
| `standalone_sender_fn` ⭐ | out-of-process delivery: cron opens a temporary connection to send when it is an independent process, and supports OAuth refresh (v0.13) |

`env_enablement_fn` / `cron_deliver_env_var` / `standalone_sender_fn` are platform-plugin hooks extracted from v0.13, making the plug-in platform **completely equal**: cron deliver, env-only setup status display, out-of-process send are all normal [1].

### Key transformation points[1]

| module | Transformation |
|------|------|
| `Platform` enum (`gateway/config.py:82-176`) | `_missing_()` accepts unknown strings, scans according to `plugins/platforms/` + runtime registry creates cache pseudo-member (`Platform('irc') is Platform('irc')` Yongzhen) |
| `GatewayConfig.from_dict` | Parse the plug-in platform name in config.yaml and no longer reject unknown platforms |
| `_create_adapter()` in `gateway/run.py` | Check the registry first, if it misses, then fall through to the built-in if/elif chain (line 5167) |
| `get_connected_platforms()` | Delegate unknown platforms to the registry |
| `PluginContext.register_platform()` | Mirror `register_tool()` / `register_hook()` mode |
| `_apply_env_overrides` | Call `entry.env_enablement_fn()` to let `gateway status` see the env-only configuration (v0.13) |

### 5 plug-in platform implementations (HEAD) [1]

| plug-in | Number of files/lines | key capabilities |
|------|------------|---------|
| `plugins/platforms/irc/` | adapter.py | TLS asyncio, zero external dependencies (v0.11.0) |
| `plugins/platforms/teams/` | adapter.py (1197) + standalone `plugins/teams_pipeline/` (2436) | Bot Framework + MS Graph, meeting held / transcribed / abstract (v0.14.0) |
| `plugins/platforms/google_chat/` | adapter.py (3342) + oauth.py | Chat API + OAuth (v0.13.0, 20th platform) |
| `plugins/platforms/line/` | adapter.py (1638) | LINE Messaging API（v0.14.0） |
| `plugins/platforms/simplex/` | adapter.py (746) | Decentralized, no user ID (v0.14.0) |
| `plugins/platforms/ntfy/` | adapter.py (582) + plugin.yaml (56) | HTTP streaming subscribe + POST publish; zero additional dependencies; **81 new tests**; passed on 2026-05-23 `b10f17b`→`6a8e131`→`3b096d6` Three commit chains were implemented (first built-in, then refactored into a plug-in, and then reinforced 401/404 fatal-error exposure) |

### Subsequent plug-in platform (v0.12 → v0.14) [1]

- **Microsoft Teams** (`plugins/platforms/teams/` + `plugins/teams_pipeline/`, v0.12.0 full link, v0.14.0 end-to-end) - Microsoft Graph full stack (`tools/microsoft_graph_auth.py` + `tools/microsoft_graph_client.py` + `gateway/platforms/msgraph_webhook.py`) [1]
- **Google Chat** (`plugins/platforms/google_chat/`, v0.13.0) - 20th platform [1]
- **LINE** (`plugins/platforms/line/`, v0.14.0) —— Japan, Korea and Taiwan[1]
- **SimpleX Chat** (`plugins/platforms/simplex/`, v0.14.0) - Privacy-first decentralization[1]
- **ntfy** (`plugins/platforms/ntfy/`, 2026-05-23) - HTTP-only push notifications, 23rd platform [1]

### Discord channel history backfill (v0.14.0+)[1]

`gateway/platforms/discord.py:3683,3692,4784`: **Read back recent messages** for context when joining a Discord channel/thread for the first time, to avoid "what were we talking about". [1] is enabled by default.

### Cross-platform unified allowlist (v0.13.0+)[1]

`allowed_channels` / `allowed_chats` / `allowed_rooms` configuration covers Slack, Telegram, Mattermost, Matrix, DingTalk (`gateway/platforms/dingtalk.py:392-496`) - unified hard gate ACL[1].

### Discord DM Role Guild-scoped (v0.13.0+)[1]

`gateway/platforms/discord.py:508 dm_role_auth_guild`, `:2206-2235`: Closed CVSS 8.1 cross-guild DM bypass. The allow list is bound to a specific guild and is no longer borrowed by other servers [1].

### WhatsApp rejects strangers by default (v0.13.0+) [1]

`gateway/platforms/whatsapp.py:236-239`：`dm_policy: open | allowlist | disabled`（默认 open，但 SECURITY release notes 提及"strangers rejected by default" —— 配合 `allow_from`/`group_allow_from` 白名单使用）。`group_policy` sync control group [1].

### Native button UI for `clarify`（v0.14.0+）[1]

`tools/clarify_gateway.py:48`: Telegram + Discord adapter override `send_clarify`, rendering inline button (such as Telegram `InlineKeyboardMarkup`). Tap for instant answers, especially on mobile devices [1].

### `[[as_document]]` Skill Media Routing Command (v0.13.0+) [1]

`gateway/run.py:11159,11163` + `gateway/platforms/base.py:2133,2154-2157,3160-3174`: skills can add `[[as_document]]` to the content to force the gateway to deliver the output as a document (instead of an inline message) [1] on supported platforms.

### Platform plug-in 12 integration points fully covered[1]

`feat: complete plugin platform parity` (2e20f6ae2) + `feat: final platform plugin parity` (e464cde58) makes the plug-in platform behave the same as the built-in platform:
- webhook delivery, PLATFORM_HINTS, `get_connected_platforms`, cron delivery, dynamic toolset generation, setup wizard, etc. [1]
- Bundled plug-in platforms (such as IRC, Teams, LINE, Google Chat) are automatically loaded when they start (`feat(plugins): bundled platform plugins auto-load by default`, 4d36349) [1]

### bundled platform plugins (v0.12.0+) [1]

Platform plug-ins released with source code in the `plugins/platforms/` directory:

| Plug-in directory | platform | Key source code | Remark |
|---------|------|---------|------|
| `irc/` | IRC | `adapter.py` | First reference implementation, zero external dependencies |
| `teams/` | Microsoft Teams | `adapter.py` (Bot Framework) | Adaptive Card approval, threading via `app.reply()`, local images through attachment (to avoid Markdown link rendering failure) |
| `line/` | LINE | `adapter.py` (LINE Messaging API SDK) | Free reply token priority + Push API guarantee; slow response (`LINE_SLOW_RESPONSE_THRESHOLD` seconds, default 45s) Push Template Buttons postback to allow users to re-obtain free tokens |
| `google_chat/` | Google Chat | `adapter.py` + `oauth.py` | Pub/Sub pull (same form as Slack Socket / Telegram long-poll, no public URL required); `/setup-files` per-user OAuth enables native file attachments |

### Multi-Platform Access Control (v0.13.0)[1]

`allowed_channels` / `allowed_chats` / `allowed_rooms` configuration items are extended to Slack, Telegram, Mattermost, Matrix, DingTalk (`#21251`) [1].

Source code verification:

- `gateway/platforms/slack.py:_slack_allowed_channels()` (line 3010)[1]
- `gateway/platforms/mattermost.py:712` `allowed_channels` / `MATTERMOST_ALLOWED_CHANNELS`[1]
- `gateway/platforms/dingtalk.py:_dingtalk_allowed_chats()` (line 392)[1]

When it is not empty, it acts as a **hard whitelist** - all messages received from channels/chat/rooms that are not in the table are discarded and no response is given to [1].

### Security: Discord role-allowlist changed to guild-scoped(v0.13.0)[1]

`gateway/platforms/discord.py:2130` Comment direct quote:

> Voice inputs always originate from a specific guild (guild_id is in scope). Pass it so role checks are guild-scoped and not cross-guild.

Fix cross-guild DM bypass in CVSS 8.1: Previously the role allowlist was *global* - roles from guild A could open doors for users from guild B. Now `_is_allowed_user(user_id, guild=..., is_dm=...)` must pass guild context (`discord.py:2134`, `2349`) [1].

### `[[as_document]]` Media Routing Command (v0.13.0) [1]

`gateway/platforms/base.py:2095-2119`: When the `[[as_document]]` string appears in the skill output, gateway changes all image attachments to **document delivery** (applicable to Signal/some enterprise platforms that need to retain the original image details), and then strips the command string from the visible text. One declaration covers all image paths [1] in the response.

### gateway = pluginhost(v0.12.0+)[1]

Starting from v0.12.0, gateway officially becomes **plugin host**:
- Drop-in messaging adapter lives outside core[1]
- Microsoft Teams is the first plugin-shipped platform (v0.12.0 introduced, v0.14.0 completed end-to-end) [1]
- Third-party adding new platform** does not need to fork the warehouse**, just drop `plugins/platforms/<name>/` directory [1]

## Platform Adapter Base Class[1]

```python
# gateway/platforms/base.py
class BasePlatformAdapter(ABC):
    """平台适配器基类"""
    
    def __init__(self, config: dict, gateway):
        self.config = config
        self.gateway = gateway
        self.platform_name = self.__class__.__name__.lower()
    
    async def start(self):
        """启动平台连接"""
        raise NotImplementedError
    
    async def stop(self):
        """停止平台连接"""
        raise NotImplementedError
    
    async def send_message(self, chat_id: str, text: str, **kwargs):
        """发送消息"""
        raise NotImplementedError
    
    async def handle_message(self, event: MessageEvent):
        """处理接收消息"""
        await self.gateway.process_event(event)
```

## Message processing flow[1]

```
用户发送消息
  ↓
平台适配器接收
  ↓
创建 MessageEvent
  ↓
GatewayRunner.process_event(event)
  ↓
解析斜杠命令（如果有）
  ↓
查找或创建 Session
  ↓
调用 AIAgent
  ↓
获取响应
  ↓
通过平台适配器发送回复
```

## Session Management[1]

```python
# gateway/session.py
class SessionStore:
    """对话持久化存储"""
    
    def get_or_create_session(self, chat_id, platform):
        """获取或创建会话"""
    
    def save_session(self, session_id, messages):
        """保存会话"""
    
    def get_session(self, session_id):
        """获取会话"""
```

## Slash command[1]

Slash command system shared with CLI:

| Order | describe |
|------|------|
| `/new` | new conversation |
| `/reset` | Reset conversation |
| `/model [provider:model]` | Switch model |
| `/personality [name]` | Set personality |
| `/retry` | Retry last time |
| `/undo` | Undo last time |
| `/compress` | Compression context |
| `/usage` | Check token usage |
| `/insights [days]` | Use insights |
| `/skills` | Browsing skills |
| `/stop` | Interrupt current work |
| `/status` | Platform status |
| `/sethome` | Set up the main platform |
| `/handoff` | Cross-platform session transfer (`gateway/run.py` `_handoff_watcher` / `_process_handoff`, poll state.db for pending sessions and rebind to target platform) |

### Command rating by platform[1]

`gateway/slash_access.py` provides per-platform/chat-type scoped slash command access control (`SlashAccessPolicy`):

- `allow_admin_from` — List of administrator user IDs that can run all registered slash commands [1]
- `user_allowed_commands` — Whitelist of command names that non-administrator users can run (if not set, non-administrators will not have any command permissions) [1]
- Group scope has independent `group_allow_admin_from` / `group_user_allowed_commands`[1]
- If `allow_admin_from` is not set for a scope, the command hierarchy for that scope remains disabled (the behavior remains unchanged), and the operator needs to explicitly list at least one administrator before [1] is enabled.

## DM pairing[1]

Control who can talk to the bot via the `GATEWAY_ALLOWED_USERS` environment variable:

```bash
# 允许的 Telegram 用户 ID
GATEWAY_ALLOWED_USERS=telegram:123456789,discord:987654321
```

When an unauthorized user sends a message, the bot will not respond (silently ignore) [1].

## Media processing[1]

```
用户发送图片/文件
  ↓
平台适配器下载
  ↓
保存到临时目录
  ↓
传递给 Agent（vision_analyze 或文件处理）
  ↓
Agent 响应包含 MEDIA: 路径
  ↓
提取本地文件
  ↓
通过平台原生方式发送
```

## Deliverable mode (deliverable artifacts) [1]

Gateway no longer only sends pictures/videos inline, but intelligently routes by file type ("deliverable mode") [1].

- **File Partition**: `extract_local_files` (`gateway/platforms/base.py:2158`) will identify the naked local file path from the Agent response text. The routing partition is located at `gateway/platforms/base.py:3258-3333`:
  - **Send inline**: Only pictures and videos (displayed inline when supported by the platform) [1].
  - **Native upload**: PDF, docx/xlsx/pptx, compressed packages, audio, html, etc. will all be sent to `send_document` as file attachments and sent to [1].
- **Supported document types**: `SUPPORTED_DOCUMENT_TYPES` is now a dict (`gateway/platforms/base.py:815-836`) mapping extensions to MIME types, including pdf/md/txt/csv/log/json/xml/yaml/yml/toml/ini/cfg/zip/docx/xlsx/pptx, and added `.ts`, `.py`, `.sh` (all `text/plain`)[1].
- **Kanban product delivery**: The `kanban_complete` tool adds the `artifacts` parameter (file path list), and Gateway uploads these products to the user [1] through `_deliver_kanban_artifacts` (`gateway/run.py`).

## Gateway service management[1]

### Linux (systemd)

```ini
# ~/.config/systemd/user/hermes-gateway.service
[Unit]
Description=Hermes Agent Gateway
After=network-online.target

[Service]
ExecStart=/path/to/hermes gateway run
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

```bash
hermes gateway start    # 启动服务
hermes gateway stop     # 停止服务
hermes gateway status   # 检查状态
```

Service unit: `hermes-gateway.service` or `hermes-gateway-<profile>.service`[1]

### macOS (launchd)[1]

```xml
<!-- ~/Library/LaunchAgents/com.nousresearch.hermes-gateway.plist -->
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.nousresearch.hermes-gateway</string>
    <key>ProgramArguments</key>
    <array>
        <string>/path/to/hermes</string>
        <string>gateway</string>
        <string>run</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

```bash
hermes gateway start    # 启动 launchd 服务
hermes gateway stop     # 停止
hermes gateway status   # 状态
```

Tag: `com.nousresearch.hermes-gateway`[1]

## Automatically restart during update [1]

The `hermes update` command automatically:
1. Discover all running gateway services[1]
2. Restart systemd/launchd service[1]
3. Stop manual process in non-service mode[1]

### Per-platform restart notification opt-out (v2026.5+) [1]

`PlatformConfig.gateway_restart_notification` (default `True`) covers **three lifecycle ping**:

1. **Pre-restart drain notification**: `⚠️ Gateway restarting — Your current task will be interrupted...`, sent to all active sessions + home channel (`gateway/run.py:2462, 2500`)
2. **Restart completed ping**: `♻ Gateway restarted`, sent to the chat that triggered `/restart` (`gateway/run.py:11406`)
3. **Start ping**: `♻️ Gateway online`, send to home channel (`gateway/run.py:11465`)

Design motivation: **operator vs end-user surfaces**. It is reasonable for back-channels like Telegram to retain ping; the Slack workspace shared with end users reads "Gateway restarting" as "the bot is broken", and the operator should be able to consistently disable three types of noise:

```yaml
slack:
  gateway_restart_notification: false
```

## Platform Specific Function[1]

### Telegram[1]
- Support group and private chat
- Group messages need to be triggered by @mention
- Voice message transcription
- Sticker support
- Topic/thread support
- **Agent Support** (v0.10.0): `TELEGRAM_PROXY` environment variable or `proxy_url` in `config.yaml`
- **Link Preview Control** (v0.10.0): `config.yaml` Medium `telegram.disable_link_preview` Turn off message link preview
- **clarify inline keyboard button** (#24199, v2026-05-15+): The clarify tool in gateway mode presents options through the Telegram inline keyboard button. `gateway/run.py` now passes `clarify_callback` to `AIAgent`; `tools/clarify_gateway.py` is an event-driven primitive (register/wait_for_response/resolve_gateway_clarify, per-session FIFO + `threading.Event` blocking). `gateway/platforms/base.py` provides abstraction `send_clarify` with numbered text backing, available out of the box with all adapters (Discord, Slack, WhatsApp, Signal, Matrix, etc.)
- **Native draft streaming** (Bot API 9.5+, v2026-05-10+): Implement streaming draft of DM reply through `sendMessageDraft`, smooth animation preview when token arrives, replacing the old `editMessageText` polling path
- **Status message in-place edit** (#30864/PR #30141, commit `9acf949`, 2026-05-23+): lifecycle/compression/context-pressure status callback no longer appends new bubbles each time. `gateway/platforms/telegram.py:1915-1946 send_or_update_status()` maintains the `{(chat_id, status_key) → message_id}` cache (`telegram.py:471-474 self._status_message_ids`), the first `send`, the same key `edit` in the subsequent, the cache is lost when edit fails and fallsback fresh send. `gateway/run.py` takes this path in `_status_callback_sync` (when the adapter supports it), otherwise falls back to `adapter.send()`. +5 test coverage first send / edit / failure-fallback / cross key & chat isolation

### Discord
- Support server and private chat
- Requires @mention or DM
- Voice channel support
- Opus audio encoding
- Slash commands integration
- **Role Permission Control** (v0.10.0): `DISCORD_ALLOWED_ROLES` environment variable, comma separated Role ID. There is an OR relationship with `DISCORD_ALLOWED_USERS` - if either user ID or role matches, it will be allowed, if neither matches, everyone will be able to use it.
- **channel_prompts** (v0.10.0): Inject different system prompts by channel/topic, also extended to Telegram (group/forum topic), Slack, Mattermost
- **@everyone and role ping blocking**: `allowed_mentions` blocks bots from triggering global notifications by default
- **Any attachment reception**: `allow_any_attachment` configuration item allows receiving attachments that are not in the whitelist type (untyped file path)
- **Channel history backfill**: enabled by default, injects recent channel history (by user + thread) into the shared session to avoid fully scanning `channel.history()` for each hot path, controlled by `history_backfill` / `history_backfill_limit`
- **choices rendered as buttons**: In multi-select mode (`choices` is not empty), each option is rendered as a Discord button
- **thread_require_mention**: The `thread_require_mention` configuration item requires messages within the thread to be triggered by @mention.

### DingTalk DingTalk
- Stream protocol connection
- **QR code scanning authentication** (v0.10.0): `hermes_cli/dingtalk_auth.py` (line 292) implements Device Flow - the terminal renders the QR code, and the user scans the code with DingTalk to automatically obtain AppKey/AppSecret without manually creating an application.
- **require_mention + allowed_users permission control** (v0.10.0): aligned with Telegram/Discord
- Support dingtalk-stream 0.24+ SDK and oapi webhooks

### WeChat
- SILK encoded voice reply (v0.10.0)
- Media attachment extraction and sending
- Native Markdown rendering
- CDN Whitelist SSRF Protection (Security Fixes)
- macOS SSL certificate repair

### WhatsApp
- Requires WhatsApp Bridge (Node.js)
- Group messages require prefix triggering
- Allow list control
- **JID/LID alias cross-shape stable pairing** (commit `52a368f`, 2026-05-23+): WhatsApp will drift between the two user identifiers `xxx@s.whatsapp.net` (JID) and `xxx@lid` (LID). `gateway/pairing.py:124-140 _user_id_aliases()` collapses all aliases of the same user into a set, `_user_ids_match()` uses set intersection to determine equality; `approve_pair` and the list/lookup path (`pairing.py:377-378`) register both LID/JID forms into the `{platform}:{alias}` index through `expand_whatsapp_aliases`, and approval will not be invalidated because the peer identifier is cut. +73 tests covering various cross-shaped scenarios

### Home Assistant
- Smart home event monitoring
- Device control
- Automation trigger

### Gateway operation and maintenance enhancement (v0.10.0)
- **Agent Cache LRU + Idle TTL Elimination**: `_agent_cache` Add upper limit and idle timeout to prevent long-running gateway memory leaks
- **Temporary agent shutdown**: Automatically close the temporary agent after the one-time task is completed
- **WebSocket Reconnection waiting**: Wait for reconnection to complete before sending to avoid losing messages.

### v0.12.0+ enhanced (2026-04-30 ~ 2026-05-13)

- **i18n internationalization** (c391684): `agent/i18n.py` introduces the lightweight i18n framework, `locales/<lang>.yaml` 16 languages ​​(en, zh, ja, de, es, fr, tr, uk, af, ga, hu, it, ko, pt, ru, zh-hant). Only the **highest impact** static user plane strings (approval prompts, several gateway slash command replies, restart-drain notifications) are covered, and agent output/logs/tool ​​results remain in English. Language parsing order: `lang=` parameters → `HERMES_LANGUAGE` env → `display.language` config → `"en"`.
- **i18n also covers web dashboard** (PR #22914 is implemented together).
- **Telegram /topic (DM topic mode)** (d6615d8, d35efb9): Create a pseudo topic (forum topic) managed by Hermes through `/topic <name>` in the private chat, and each topic is an independent session. `/topic off` exit, `auth gate + screenshot debounce`, CASCADE delete, rename guard, General-topic processing. See [Gateway Session Management](gateway-session-management.md) for details.
- **Telegram native draft streaming** (4ed293b, Bot API 9.5+): Stream output through `sendMessageDraft` instead of editing existing messages to avoid rate limits caused by repeated editing.
- **Telegram cadence tuning + adaptive fast-path** (ac95b8c): Short replies take the fast path, long replies take the smooth rhythm, corresponding to `tests/.../adaptive text-batch tiers`.
- **Telegram edit overflow split-and-deliver** (bf1f409): Ultra-long edits are no longer silently truncated, but split into multiple deliveries.
- **Telegram `clarify` inline keyboard** (29d7c24): Map the multiple options of the `clarify` tool to inline keyboard buttons, and the user clicks to backfill directly.
- **Telegram DM group allowlist** (1f71217): Group user allowlist is also supported in DM mode and the pre-#17686 chat-ID-in-_USERS configuration is retained.
- **QQBot guild ACL fix** (d69a0b2): guild messages and guild DMs also undergo ACL checking, blocking the allowlist bypass.
- **QQBot Health Repair Cluster** (2026-05-23+, Tencent Team @walli):
  - `bbd77d1` —— `_send_identify` adds `INTERACTION` intent bit (`1<<26`). The `INTERACTION_CREATE` event originally triggered by approval-button click is not dispatched by the gateway at all; the video/file attachment description has a local cached path to facilitate LLM reference file postback.
  - `a54f5af` —— `gateway/platforms/qqbot/adapter.py` handles WS opcode 7 (Server Reconnect: turn off WS to trigger reconnection, use Resume to retain the session) and opcode 9 (Invalid Session: see the `d` field to determine resumable, only clear the session when false); delete 4009 (the connection timeout is resumable, and the session should not be cleared); extend fatal close set to 4001/4002/4010-4014 (meaningless retry and stop)
  - `0e7448d` —— `_download_and_cache(original_name=...)` uses the attachment metadata original file name, and no longer uses the CDN hash name (the previous file name was `qqdownload_...oadftnv5`)
  - `60b0a0e` —— `_guess_ext_from_data` / `_looks_like_silk` Change `data[:5/4]` to `data[:6]`. The original slice length is not long enough to match the 6-byte literal `#!SILK`, which depends on the 9-byte `#!SILK_V3` and 2-byte `0x02!`.
- **Signal multi-device group message processing** (e713932): Group messages sent by linked devices via the syncMessage path are now processed correctly.
- **Weixin content fingerprint deduplication** (7a8ee8b): Duplicate webhook delivery of the same content is skipped through fingerprint.
- **WeCom AES key automatic padding** (8f4c0bf): Base64 AES key is automatically padded before decoding, compatible with upstream format differences.
- **gateway audio routing centralization + FLAC support** (aa7bf32): All platforms share a unified audio routing table (`gateway/platforms/base.py:_AUDIO_EXTS`), and a new `.flac` is added; Telegram automatically documents fallback for formats that are not natively supported (`.wav`/`.flac`).
- **gateway multi-image sending**: `send_multiple_images` uses the native album/group API (3de8e21) on Telegram, Discord, Slack, Mattermost, and Email; Signal also completes multiple images (04ea895).
- **stream-consumer thread context reserved** (ff14666 + e164a9c): Message overflow/first message is no longer lost when sending thread routing.
- **stream-retry diagnosis** (68e4464 + 126cbff): drop log carries upstream + timing to facilitate locating which provider is shaking; fold two lines at the same time and drop status into one line to avoid noise.
- **gateway shutdown forensics** (cede612): non-blocking diag, per-stage timing, stale unit warning.
- **gateway WSL interop PATH reserved** (8ab9f61): WSL interop PATH is reserved in the systemd unit to prevent `wsl.exe` from being invisible.
- **gateway status version detection** (d90f73b): Use git HEAD SHA as the basis for stale-code checking (replacing file mtime, CI friendly).
- **gateway scoped-lock stale detection** (fb1f409, 653d304): When start_time is missing (macOS), use cmdline comparison; when cmdline is unreadable, fall back to lock record argv.
- **gateway kanban notification deduplication** (861ce7c, a96dd54): blocked/gave_up status deduplication, sending exception rewind, re-block notification delivery.
- **per-platform admin/user slash command split** (a282434): Administrator commands and user commands are registered to different menus.
- **per-platform reply_to_mode** (6b76ea4): Discord/Telegram read reply_to_mode from config.yaml instead of just env.

### v2026.4.18+ enhanced

- **Enterprise WeChat (WeCom) QR code scanning authentication**: The setup wizard (`hermes_cli/gateway.py:_setup_wecom`) obtains the bot credentials by scanning the `gateway.platforms.wecom.qr_scan_for_bot_info` code, no manual configuration is required
- **Plug-in slash command cross-platform nativeization**: The plug-in command of `register_command()` is automatically exposed as Discord native slash, Telegram BotCommand, and Slack `/hermes` subcommands, without the need to repeat the implementation for each platform
- **Decision-type command hook**: `command:<name>` hook can return `{"decision": "deny"|"handled"|"rewrite"|"allow"}` intercepts before core processing
- **Slack reaction life cycle**: `SLACK_REACTIONS` environment variable switch controls the bot's reaction when sending and receiving messages (emoji)
- **Feishu @mention context preserved**: Inbound messages retain @mention context
- **Fixed line breaks in Feishu streaming editing**: Streaming output is no longer preceded by extra blank lines
- **Session state maintenance**: `hermes_state.py` adds `maybe_auto_prune_and_vacuum()`, which is executed idempotently at startup (the last running time is recorded through the `state_meta` table across processes). Prevent sessions and FTS5 indexes from growing indefinitely (one heavy user reported 384MB/982 sessions impacting performance, dropped to 43MB after prune + VACUUM)
- **MEDIA: Tag extension**: Supports automatic extraction of PDF, document, and archive extensions
- **Global Tunnel/Proxy Scenario URL Switch**: `security.allow_private_urls`/`HERMES_ALLOW_PRIVATE_URLS` Allows resolution of private IP ranges (198.18.0.0/15, 100.64.0.0/10), resolves OpenWrt/TUN Proxy (Clash/Mihomo/Sing-box)/Enterprise VPN/Tailscale scenarios. Cloud metadata endpoints (169.254.169.254, etc.) are always blocked
- **Platform hints**: `PLATFORM_HINTS` covers the system prompts of Matrix, Mattermost, and Feishu

### v2026.5.x Enhanced

#### New Platform Plugins (5 bundled)

SimpleX, LINE, Google Chat, and Microsoft Teams are all connected in the form of bundled plug-ins (`plugins/platforms/<name>/adapter.py` + `plugin.yaml`, registered through `ctx.register_platform()`), and the core gateway code has zero changes. There is also the core adapter `gateway/platforms/msgraph_webhook.py`. `PlatformEntry` now exposes the common plugin hooks `env_enablement_fn` (which automatically injects environment variables when enabled) and `cron_deliver_env_var` (the home-channel target of cron `deliver=`).

#### admin/user classification for slash commands (`gateway/slash_access.py`)

The new module `SlashAccessPolicy` dataclass distinguishes slash commands executable by administrators and ordinary users:

| Dimensions | DM configuration key | Group configuration key |
|---|---|---|
| Admin source | `allow_admin_from` | `group_allow_admin_from` |
| Available commands for users | `user_allowed_commands` | `group_user_allowed_commands` |

`is_admin()` / `can_run()` make judgments, and `_ALWAYS_ALLOWED_FOR_USERS` is a whitelist. Entry `policy_from_extra()` / `policy_for_source()`.

#### `/handoff` — Cross-platform session transfer

The CLI marks the session in `state.db` as `handoff_state='pending'`. `gateway/run.py`'s `_handoff_watcher()` (2-second polling) claims the record to be transferred through `claim_handoff()`, `_process_handoff()` calls the target platform adapter's `create_handoff_thread()` (Telegram rewrites to create a forum topic), delivers the transfer notification with `user_id="system:handoff"`, and finally marks `completed`/`failed`. Allows a conversation to "relay" from the CLI to a chat platform.

#### i18n static text localization (`agent/i18n.py`)

`t(key, lang, **kwargs)` + `get_language()`, catalog is loaded flat from `locales/<lang>.yaml`. Currently available in **16 languages**: af, de, en, es, fr, ga, hu, it, ja, ko, pt, ru, tr, uk, zh, zh-hant. `display.language` Configure static message translation, gateway commands and web dashboard have been localized.

#### Shut down evidence collection (`gateway/shutdown_forensics.py`)

`snapshot_shutdown_context()` Snapshots within <10ms when SIGTERM/SIGINT is received `/proc` finds out the signal sender, `spawn_async_diagnostic()` non-blockingly outputs per-phase timing and stale-unit warnings, `check_systemd_timing_alignment()` checks whether systemd timeout configuration is reasonable.

#### Automatically resume interrupted sessions

Automatically restore interrupted sessions after gateway restarts/crash. The logic is in `gateway/session.py` (`mark_resume_pending()` / `clear_resume_pending()`, `resume_reason="restart_interrupted"`) and `gateway/run.py` (`resume_pending` persistent mark + freshness guard to prevent stale tool-tail from resurrecting old tasks).

#### Channel whitelist

`allowed_{chats,channels,rooms}` whitelist extends to Telegram, Slack, Mattermost, Matrix, DingTalk, LINE, and `gateway/config.py` maps YAML keys to environment variables (such as `SLACK_ALLOWED_CHANNELS`, `TELEGRAM_ALLOWED_CHATS`, `LINE_ALLOWED_{USERS,GROUPS,ROOMS}`).

#### Telegram enhanced

- **Native draft streaming**: `send_draft()` uses Bot API 9.5's `sendMessageDraft`, reuses `draft_id` for animated preview, only private chat.
- **clarify inline keyboard**: `send_clarify()` renders multi-select clarification into `InlineKeyboardMarkup` button callback (approval/update prompts are also reused).
- **guest mention mode**: Under `TELEGRAM_GUEST_MODE`, non-whitelisted group members can only trigger the bot through explicit @mentions.
- **Notification Mode**: `notifications` configures `important`/`all`, and silently sends intermediate push (`disable_notification=True`) unless `metadata["notify"]=True`.
- **Group slash command reserved** (`9451087`, 2026-05-24): The slash command observed in the group is no longer silently swallowed (`gateway/platforms/telegram.py:+6 行` + 34 lines of new tests).

#### 2026-05-24 Platform details repair cluster

- **Webhook routing fail closed + Svix signature** (`bbf02c3`/`dbf73e9`/`15aa688`): See the paragraph with the same name in `[Security Defense System](security-defense-system.md)` - `gateway/platforms/webhook.py:383-395 + 690+` adds Svix signature + missing secret and returns 403.
- **MSGraph Webhook forces client_state** (`4ca77f1`, #30169): `msgraph_webhook.py:133-145` connect rejects `_client_state is None`; `:316 _validate_client_state()` returns False when expected is None (previously True was equivalent to allowing all unconfigured secrets).
- **Feishu auth triple** (#30739/#30744/#30746 + `f378f00`): `gateway/platforms/feishu.py` URL verification token precedes challenge echo + webhook secret mandatory + approval button chat-binding.
- **QQBot approval button session-owner authorization** (`3e78e35`, #30737): `qqbot/adapter.py:+54`.
- **Discord role allowlist bypass removal** (`c3caca6`, #30742): `gateway/run.py:6329-6341` remove early return.
- **DingTalk Default allow-all cancel** (`1f897b0`, #30743): `hermes_cli/gateway.py:_setup_dingtalk` no longer automatically writes `DINGTALK_ALLOW_ALL_USERS=true`.
- **DingTalk finalize the streaming card before disconnecting** (`39b8d1d`): `gateway/platforms/dingtalk.py:+13` should be `_close_streaming_siblings` before `_http_client.aclose()` to prevent the AI ​​Card from getting stuck in the streaming state.
- **WeCom flush cancel-delivery race protection** (`5848174`): `gateway/platforms/wecom.py:619-628 _flush_text_batch` Add `_pending_text_batch_tasks.get(key) is not current_task` synchronization check, close the message silently dropped window when sleep/cancel overlaps (+89 lines of test).
- **WeCom-callback token expires and automatically refresh** (`21db250`): When errcode 40001/42001, evict cache + retry with a new token once (previously, the token was not changed until TTL 7200s).
- **Gateway debouncer + CodeQL log minimization** (`7abd627` + `1bed4e8`): `gateway/platforms/base.py:4-7` debounce debounce log deletes `event.text[:60]` slices and changes to `text_len=...`.
- **Plugin transform_llm_output Streaming Visibility**: See the `[Interrupt And Fault Tolerance](interrupt-and-fault-tolerance.md)` "Streaming Completion Visibility" chapter - `gateway/run.py:17680-17717` `_transformed=True` edits streamed messages in-place instead of sending duplicates to avoid plugin modifications being invisible.

### Comparison with other Agent frameworks

| characteristic | Hermes | OpenClaw | Claude |
|------|--------|----------|--------|
| Number of platforms | 23 (17 built-in + 6 plug-ins) | 14+ | 1 |
| Unified gateway | single process | support | N/A |
| session sharing | Cross-platform | support | N/A |
| speech transcription | Telegram/Discord | support | N/A |
| Group support | Multi-platform | support | N/A |
| Service management | systemd/launchd | support | N/A |

## Gateway Proxy Mode (thin relay mode, 2026-04-14)

Usually Gateway and Agent run in the same process: Gateway receives messages → directly calls `AIAgent.run_conversation()`. **Proxy mode** separates the two - Gateway only does platform I/O (encryption, sharding, media), and all Agent work is forwarded to the remote Hermes API server.

### Typical uses

```
[Matrix/Discord/...]  ←→  [Gateway (Linux Docker, E2EE keys)]
                                    │ POST /v1/chat/completions (SSE)
                                    ↓
                              [Hermes API server (macOS host)]
                                    │
                                    ↓
                     本地文件、memory、skills、统一 session store
```

**Problem solved**: I want to use Matrix E2EE, but E2EE requires persistent encryption keys and is more stable when running in Docker; and the agent itself wants to run on the macOS host to access local files/skills/memory. It turns out that you have to choose one of the two, and proxy mode connects them.

### Activation method

```yaml
# ~/.hermes/config.yaml — 配置优先
gateway:
  proxy_url: "http://host.docker.internal:8080"
```

Or environment variables (Docker friendly, no need to hang config):

```bash
GATEWAY_PROXY_URL=http://host.docker.internal:8080
GATEWAY_PROXY_KEY=<matches upstream API_SERVER_KEY>
```

### implementation position

Starting from `gateway/run.py:7709`:
- `_get_proxy_url()` — Check env var first and then config.yaml
- `_run_agent_via_proxy()` — HTTP + SSE streaming forwarding, parsing streaming responses
- `_run_agent()` — If proxy_url is detected, go to the proxy path, otherwise go to the local agent
- `GatewayStreamConsumer` works as usual, streaming sharding is still completed on the Gateway side

### Key Features

| mechanism | illustrate |
|---|---|
| `X-Hermes-Session-Id` header | Carrying session id ensures continuity across request sessions |
| `GATEWAY_PROXY_KEY` | Matches the remote `API_SERVER_KEY` and uses Bearer authentication. |
| SSE streaming | The response comes in chunks, and Gateway streams it to the platform. |
| Wrong compatibility | The returned result dict structure is consistent with the local agent, and the session store records as usual |
| Platform independent | Not just Matrix, any platform adapter can use proxy mode |

### call chain

```
用户在 Matrix 发消息
    ↓ E2EE 解密 (Gateway 侧)
gateway.process_event()
    ↓
_run_agent() → 检测到 proxy_url
    ↓
_run_agent_via_proxy():
    POST {proxy_url}/v1/chat/completions
      + X-Hermes-Session-Id: <sid>
      + Authorization: Bearer <GATEWAY_PROXY_KEY>
      + body: { messages: [...], stream: true }
    ↓ SSE stream 到达
    逐 chunk 通过 GatewayStreamConsumer 转发到平台
    ↓ E2EE 加密 (Gateway 侧)
发送回用户
```

## Telegram DM Topic submission (2026-05-26, 6 commit cluster)

Involving 6 commits (baseline commit `415be5539`, follow-up `96c71d8c4` / `dcd504cea` / `c394e7919` / `5b1c75d66` / `27df4b388`). **Problem domain**: Telegram has both the forum topic in group/channel (thread_id > 0, chat_id < 0) and the topic in **DM private chat** (chat_id > 0). The general `DeliveryRouter.send()` path is inserted into the metadata and `thread_id` is used smoothly for group topics. ** Directly sending DM private messages to forum topics cannot pass the Telegram API **.

**Core fixes (`gateway/delivery.py` commit `415be5539`)**:

```python
def _looks_like_telegram_private_chat_id(chat_id: Optional[str]) -> bool:
    if chat_id is None:
        return False
    try:
        return int(chat_id) > 0
    except (TypeError, ValueError):
        return False
```

When `DeliveryRouter.send()` detects `target.platform == Platform.TELEGRAM and _looks_like_telegram_private_chat_id(target.chat_id)`, `thread_id` is not inserted into the general send metadata** - the DM topic takes the adapter-level direct route instead of the general thread_id forwarding.

**5 follow ups along lifecycle**:

| Commit | Behavior |
|--------|------|
| `96c71d8c4` requires anchor | DM topic delivery must have `reply_to` anchor by default (anti-spam thread) |
| `dcd504cea` automatically create | First time DM topic does not exist → adapter automatic `forum_topic_create` |
| `c394e7919` Refresh expired thread | thread_id automatically re-fetch + cache invalidate after expire on Telegram side |
| `5b1c75d66` refactor | Simplified refresh helper |
| `27df4b388` exempt anchor-required | DM topic send of `reply_to_mode=off` is not subject to anchor-required (manual exempt path) |

## Telegram table Row-Group spacing tightened (2026-05-26, fix)

`9d10c45e3 fix(telegram): tighten table row-group spacing and drop redundant first bullet`: GFM → Telegram-row-group rewriter used `"\n\n".join(rendered_rows)` before, and the multi-list mobile column exploded into a bullet section; in addition, when the table did not have a row-label column, the row heading appeared twice (standalone bold + first bullet).

Fix: Use single `\n` for heading-to-bullets in row-group, and leave an empty row between row-groups; skip the first bullet of value == heading when the table has no row-label.

## WeCom Callback defusedxml + Lazy Dep（2026-05-26，harden）

`gateway/platforms/wecom_callback.py:20-24` (commit `5744b1757`): Replace `from xml.etree import ElementTree as ET` with `import defusedxml.ElementTree as ET`. WeCom callback request body is **pre-auth untrusted**, defusedxml blocks entity-expansion / billion-laughs / XXE DoS. response-building XML does not move in `wecom_crypto.py` (does not parse from untrusted input).

Follow up `31c8d5ff5`: try/except the defusedxml import package (same as `aiohttp` / `httpx` compatibility mode), set `DEFUSEDXML_AVAILABLE` flag; `check_wecom_callback_requirements()` check flag, what is actually missing in log when dep is missing + skip adapter (no more hard import crash); `pyproject.toml` newly added `[wecom] extra` with `defusedxml==0.7.1`; `tools/lazy_deps.py` registration triggers lazy install prompt.

## 2026-05-27 wave — Telegram multiple fixes + API Server CRUD + Signal/Slack/Google Chat minor fixes

### Telegram follow-up wave

Multiple fixes are superimposed on 2026-05-26 DM topic 6:

| Commit | Behavior |
|--------|------|
| `9acf949` | **feat: edit status messages in place instead of appending (#30864)** — Edit status messages in place |
| `1ac8deb` | **feat(gateway): stream Telegram edits safely** — Streaming chunks safely edit the same message |
| `0325e18` | **fix(gateway): keep Telegram heartbeat + interim commentary on; edit heartbeat in place (#33187)** |
| `95a0955` | **fix(gateway): restore Telegram DM topic thread_id after session split (#27166)** |
| `3ec28f3` | **fix(telegram): preserve topic metadata on overflow edits** |
| `b38140e` | **fix(gateway): allow chat-scoped telegram auth without sender user_id** |
| `d81b888` | **fix(telegram): report cron topic fallback** |
| `16d8e44` | **fix(telegram): add DM topic typing fallback when message_thread_id rejected** |
| `aef297a` | **fix(telegram): skip send_chat_action for DM topic reply-fallback lanes** |
| `b323957` | **fix(telegram): preserve DM topic routing via reply fallback** |
| `ae005ec` | **fix(send_message): map Telegram General topic id to None for forum groups (#22423)** |
| `60f84c6` | **gateway: quiet Telegram operational chatter** |
| `efa9525` | **fix: ignore Telegram start pings** |
| `8807b1c` | **fix(gateway): hide telegram compaction status noise** |
| `9d789f3` | **feat: add disable_topic_auto_rename gateway flag** |
| `ad2531b` | **feat: skip-STT audio path + 2GB cap via local Bot API server** |
| `a724c3b` | **feat: pin incoming user message for duration of agent turn** |
| `c931dad` | **feat: ignore_root_dm with system command lobby** |
| `b1acf80` | **feat: support quick-command-only menus** |

### API Server CRUD (OpenAI-compatible gateway enhancement)

`gateway/platforms/api_server.py` greatly expanded (commit `f7527b0` +476 lines + #33016):

- **Session Control**: New endpoint allows external clients to CRUD sessions (prerequisite: API_SERVER_KEY Bearer)
- **`GET /v1/skills`** (#33016) - Column installed skill (name/description/category)
- **`GET /v1/toolsets`** (#33016) - column `api_server` platform resolved toolset + expanded tool name
- All protected by `API_SERVER_KEY` Bearer scheme
- `/v1/capabilities` Advertisement `skills_api` + `toolsets_api` Two new abilities (`9622326`)
- session chat API supports media input (`464b51d`)

> Solution scenario: Previously, external clients could only start the dashboard web server, or let the model list skills through chat - now it is deterministic and does not introduce model cost.

### Signal / Google Chat / Slack minor repairs

- `7f40767` **feat(signal): add `require_mention` filter for group chats**
- `c386400` **fix(security): honor relay-declared sender_type in Google Chat adapter to prevent BOT filter bypass**
- `8578f89` **test(google-chat): cover relay-declared sender_type honoring**
- `24d3216` **fix(slack): enable writable app home DMs in manifest**

### Voice-mode containerized audio bridge

- `bde487c` **fix(voice): honor `PULSE_SERVER`/`PIPEWIRE_REMOTE` inside Docker (#21203)**
- `30dd554` **fix(voice_mode): generalize container phrasing and use `$XDG_RUNTIME_DIR`**

### Gateway/SQLite Miscellaneous

- `dbafa08` **fix(cron): avoid delivery origin as sender identity**
- `e572737` **Fix cron dashboard rendering for partial jobs** + `e407376` partial job records normalize + `96dc272` getJobState helper
- `2a7047c` **fix(sqlite): fall back to `journal_mode=DELETE` on NFS/SMB/FUSE (#22043)** —— When sessions.db is running on a network shared disk, WAL is unavailable and automatically downgraded
- `78b0008` **fix(gateway): also catch restart TimeoutExpired; friendly message** + `dccf1fb` cap adapter disconnect during stop

## v0.15.1 Maintenance window increment (2026-05-31, hermes `eb3cf9750`)

### Telegram DM topic Routing double repair

#### 1. Synthetic notification retains DM topic metadata (`4259bab7d`)

`gateway/run.py` modified +109/-25 lines + `tests/gateway/test_restart_notification.py` +29/-3 + `test_update_command.py` +6/-2:

- restart / update / other gateway's spontaneous "system notification" message originally only carried the `(chat_id, thread_id)` tuple, and **lost the DM topic metadata** (topic name/topic root flag).
- After repair, when synthesizing an envelope, **completely copy the DM topic field** of the source envelope to make reply-to-mode / topic-anchor consistent.

#### 2. `_get_dm_topic_info` is parsed on the class (HEAD `eb3cf9750`)

- `gateway/run.py:12897 get_info = getattr(type(adapter), "_get_dm_topic_info", None)`
- The original instance-level `getattr(adapter, "_get_dm_topic_info")` has a false positive under the `MagicMock` test fixture: the mock automatically generates any attribute → truthy callable, and any non-dm `chat_type` + thread_id fixture takes the wrong DM topic path.
- Change it to ** only look for this method (`type(adapter).__dict__` or `getattr(type(adapter), ...)`) on class **, and mock auto-attribute will be invalid.

#### 3. Supporting links

- `gateway/run.py:14232,14251 _is_telegram_dm_topic_target` Determine routing
- `gateway/platforms/telegram.py:1292 _persist_dm_topic_thread_id` + `:1318` persistence / `:1469` automatic refresh stale thread

### WhatsApp / WeChat text debounce batch processing (`b0ce47daa` + `cddb7283d`)

- WhatsApp / The client of WeChat (Weixin / iLink) does not package messages. Forwarding or copying and pasting multiple lines will be split into multiple separate webhooks for delivery; the agent is triggered once for each message.
- Newly added **Text debounce batch processing**: Continuous text in the N ms window can be combined into a single turn.
- The configuration key is placed under `config.yaml`, per-platform; `cddb7283d` corrects the spelling of PR's config path.

### `/stop` across actors (`1044d9f25`, #35959)

In per-user thread mode (`thread_sessions_per_user=True`), the session key of each participant is `...:{thread_id}:{user_id}`. When a user `/stop` starts a run from another participant, the caller cannot be found under its own key → returns "no active task to stop". Fix: Check active runs of all participants in thread scope.

### Self-command loop defense (`5cd6c1717` + `bd72d333d`, #30719)

Three-layer defense against SIGTERM-respawn loop (generated by the interaction between agent scheduling its own gateway restart and launchd/systemd KeepAlive):

1. **`_HERMES_GATEWAY=1` env var** (set when gateway is started): `hermes_cli/gateway.py:5427` stop / `:5512` restart Reject when seeing this marker.
2. **cron regex tightening** (`bd72d333d`): Do not treat `hermes restart` as a valid cron route for users.
3. Subcommand dispatch prevents loopback.

### Nested `gateway.platforms` configuration block merge (`44f3e5186` + `6d2727ef1` + `0bfe19ba1`)

- The nested block `gateway:` → `platforms:` under `config.yaml` is not originally seen by the adapter config hook (only the top-level `platforms:` is taken).
- Three commit fixes: merge nested block + run nested-only platform hook + Discord `allow_from` clear → env var mapping.

### Watcher recovery and LRU cache reinforcement

#### Watcher batch 100 + atomic detach (`32899279a` + `0036c7292`)

- `gateway/run.py:4481-4490` watcher recovery rewrite:
  - Atomic separation of the current batch: reassign a new list instead of `clear()` to avoid concurrent append being swallowed
  - Yield event loop every 100 `await asyncio.sleep(0)` (avoid O(n²) blocking of thousands of watchers)
- `0036c7292`: plugin/bundle error log `debug` → `warning`; watcher recovery O(n²) fixed.

#### LRU cache capping (`3c21fed09` + `e8cacb57d`)

- BlueBubbles `_guid_cache` LRU capped
- Feishu `_message_text_cache` LRU capped

### Telegram httpx pool timeout retry (`dc4de1437`, #35664)

httpx pool exhaust under high concurrency → no longer silently drop messages, try again.

### other

- **send_message recognizes email target** (`d3724c0be` + `bfc4a2603`) - strings that comply with RFC5322 are used as explicit targets, and EMAIL_HOME is not forced. The error message refers to `EMAIL_HOME_ADDRESS`.
- **google-workspace Gmail header is case insensitive** (`8bd00607d`)
- **silence-narration message pre-send interception** (`45bc65abb`) - `*(silent)*` / `_silent_` / single point `.` / `...` / `silent` / silent emoji; bot-to-bot anti-loopback.
- **`fix(gateway): never auto-pause platforms on transient network/DNS failures`**（`45465b0d5`，#35387）
- **`fix(gateway): recover model on post-interrupt turn; gate fallback status`**（`2b16b756a`，#35381）
- **MEDIA tag regex supports Windows absolute paths** (`51d165a8e` + `1b955450e` + `20d073fd0`, #34632) - `(?:~/|/)` 原仅 Unix 形式；扩到 `[A-Za-z]:\\` Windows drive letter。
- **Dashboard chat WS allows insecure public network binding** (`e8076c1eb` + `234ac0093`) - non-loopback WS peers are released when explicit `--host <non-loopback> --insecure` is specified.
- **Honcho self-hosted setup paths reinforcement** (`827ce602d`)

### Security: Media delivery path neutralization

Four-layer defense chain (see [Security Defense System](security-defense-system.md) for details):

- `9b78f411c` (#35584/#35684) — mutation-verifier footer backtick wraps all paths to prevent `extract_local_files()` from accidentally uploading the rejected `config.yaml` path as a file attachment.
- `4ec0adebe` — `gateway/platforms/base.py` adds `config.yaml` denylist (belt-and-suspenders) to `validate_media_delivery_path`.
- `bdfba4524` — System tips text no longer automatically uploads local files that hit it.
- `02d1da49d` — `gateway/platforms/base.py:18-26` Block Hermes root config (`~/.hermes/`) entire directory in media delivery, test +39 lines.

---

## 2026-06-02 Incremental — Structured stream-event protocol + per-platform defaults + media caching primitives

### Structured stream-event protocol (#37250, `787936d1`)

8 files **+740/-29**. **Formally decouple** the "content" and "rendering" layers of streaming performance: the agent side emit typed events (what happens), and the adapter side render hooks (how to deliver). **Pure presentation**: Nothing is persisted to the conversation history - **No prompt cache / message-flow invariants** are broken.

#### New module `gateway/stream_events.py` (171 lines / 7 frozen dataclasses)

| OK | kind | Field |
|---|---|---|
| `:44` | `MessageChunk` | text |
| `:56` | `MessageStop` | final: bool |
| `:72` | `Commentary` | text（interim） |
| `:85` | `ToolCallChunk` | tool_name / args / preview |
| `:104` | `ToolCallFinished` | — |
| `:122` | `LongToolHint` | — |
| `:135` | `GatewayNotice` | — |

#### New module `gateway/stream_dispatch.py` (line 132)

```python
# 截自 :40-129
class GatewayEventDispatcher:
    def __init__(self, adapter, sink, enqueue_tool_line, tool_mode,
                 preview_max_len, on_long_tool, on_notice): ...

    def dispatch(self, event):                          # :88-129
        if isinstance(event, MessageChunk):
            self.adapter.render_message_event(event, self.sink)
        elif isinstance(event, MessageStop):
            self.adapter.render_message_event(event, self.sink)
        elif isinstance(event, ToolCallChunk):
            line = self.adapter.format_tool_event(
                event, mode=self.tool_mode, preview_max_len=self.preview_max_len
            )
            if line is not None:                        # None = adapter 吃掉事件
                self.enqueue_tool_line(line)
        # ... mode 过滤 "all" / "new" / "verbose" / "off"
```

#### Three new hooks (`gateway/platforms/base.py`)

| OK | method | Default behavior |
|---|---|---|
| `:1873` | `supports_draft_streaming()` | `False` ——Adapter active coverage only has native draft (currently only Telegram) |
| `:1934` | `render_message_event(event, sink)` | MessageChunk → `on_delta`、MessageStop → `on_segment_break`、Commentary → `on_commentary` |
| `:1955` | `format_tool_event(event, mode, preview_max_len)` | Return emoji + tool name + args preview, or `None` = **eating event** (plain text platform filter tool chrome) |

#### Telegram MarkdownV2 Alignment (`gateway/platforms/telegram.py`)

```python
# 截自 :2498-2542
async def send_draft(self, chat_id, draft_id, content, metadata):
    formatted = self.format_message(content)
    try:
        return await self._bot.send_message(
            chat_id, formatted, parse_mode=ParseMode.MARKDOWN_V2,
            ...
        )
    except BadRequest:                                  # MarkdownV2 解析失败
        return await self._bot.send_message(            # 回退 plain text
            chat_id, content, ...
        )
```

—— **Goodbye to the "original text → rich text" jump between the draft streaming animation and the final sendMessage**.

#### Config（`gateway/config.py`）

`streaming.transport` defaults from empty → `"auto"`: The adapter of `supports_draft_streaming() == True` automatically goes to native draft, and the others remain in edit mode (**global security**).

#### test

- `tests/gateway/test_stream_events.py` **+182**
- `tests/gateway/test_telegram_send_draft_format.py` **+114**

### Per-platform streaming default value (#37303, `195c4d2a`)

`hermes_cli/config.py:1355-1368` - No more "one global switch does everything", choose the default according to the platform characteristics:

```python
# 截自 :1365-1368
"platforms": {
    "telegram": {"streaming": True},      # 原生 sendMessageDraft 平滑 → 默认开
    "discord":  {"streaming": False},     # 重复 editMessage 闪烁 → 默认关
},
```

**Deep-merge Contract** (Empirical `:1360-1364` annotation):
- `display.platforms.discord.streaming: true` set **explicitly** by the user beats the default
- Global `streaming.enabled` master gate still `gate-all`
- The per-platform flag only takes effect after streaming is turned on

**No bump `_config_version`** - deep-merge "fills in the blanks" for old installations, **no migration required**.

**Dashboard automatically exposes toggle**: The web settings schema is generated by `DEFAULT_CONFIG`, so `display.platforms.telegram.streaming` / `.discord.streaming` are automatically exposed with boolean toggle - **zero changes** to the front end.

Test: `tests/hermes_cli/test_per_platform_streaming_defaults.py +65`.

Supporting `d78d77e4 feat(config): surface gateway streaming block in DEFAULT_CONFIG (#37285)` - At the same time, insert the entire gateway streaming block into DEFAULT_CONFIG so that the dashboard can also be edited.

### Platform-independent media caching primitives (`f768e75e` + `fa3b06b0`)

`gateway/platforms/base.py:1313-1366 cache_media_bytes(data, filename, mime_type, default_kind)` —— **Any adapter reuse**:

```python
# 截自 :1313-1366
def cache_media_bytes(data, filename, mime_type, default_kind):
    ext = _resolve_extension(filename, mime_type)
    safe_name = _sanitize_filename(filename)
    if is_image(ext): return cache_image(data, safe_name)
    if is_video(ext): return cache_video(data, safe_name)
    if is_audio(ext): return cache_audio(data, safe_name)
    return cache_document(data, safe_name, kind=default_kind)
    # 返 CachedMedia 含 sandbox-translated agent-visible 路径
    # （to_agent_visible_cache_path 防带空格路径泄）
```

**Telegram access** (`gateway/platforms/telegram.py`): observed-group path size-gate → download → `cache_media_bytes()` → annotate; `_media_message_type()` assists in merging addressed-media type ladders.

**Benefits**: Any adapter (Discord/Slack/Signal/…) can be reused directly, **Write a detailed description of the entire platform**.

### Extract-stripped tool response recovery + final-delivery convergence (#29346, `a1f76ba7` + `8bf498c2`)

| OK | change |
|---|---|
| `:1748-1761 _strip_media_directives(text)` | New helper, strip `[[audio_as_voice]]` / `[[as_document]]` / `MEDIA:<path>` |
| `:4082-4083 _response_pre_extract = response` | **Snapshot** before extract_media/extract_images/extract_local_files |
| `:4114-4126` | **Empty text + no attachment** after extraction → Restore from post-`extract_media` body (MEDIA has stripped the space path) |
| `:4120-4125 response_delivery_recovered` | WARNING contains pre-extract size + target chat_id |
| `:4179-4200` | Text exists + non `_tts_caption_delivered` → send; mark final response is notification delivery |
| `:4333 response_delivery_dropped` | **ERROR**: The response is not empty but nothing is sent - loudly maintain the invariant |

Test `tests/gateway/test_tool_response_drop_recovery.py +258`.

### Weixin `asyncio.wait_for` replaces aiohttp ClientTimeout (`56666901` + `765790a2`)

`gateway/platforms/weixin.py:370-414` —— `_api_post` / `_api_get` Use `asyncio.wait_for(_do(), timeout=timeout_ms/1000)` instead, and fix the error that aiohttp cannot find the `"context manager should be used inside a task"` of the running task in the cron `run_coroutine_threadsafe()` context. `:405-407` Comments out the crucifixion scene. `_get_updates()` + `_do_upload/_download()` is now unified as `wait_for` mode.

Test `tests/gateway/test_weixin.py +145`.

### Gateway Miscellaneous

- `f7a3509b fix(gateway): honor WECOM_ALLOWED_USERS in env-only WeCom DM allowlist` —— `wecom.py:165-171` plus `os.getenv("WECOM_ALLOWED_USERS", "")` fallback branch
- `0cd5867b fix(whatsapp): honor dm_policy and group_policy open at the gateway`
- `eee32cdd fix(gateway): fall back to in-process heartbeat when s6 sleep is missing (#36208)` —— `hermes_cli/gateway.py +59` + `tests/hermes_cli/test_gateway_s6_dispatch.py +143 / -34`
- `b14e15c48 fix(gateway): clean service restart notifications` - 9 files **+378 / -34** (`gateway/run.py +198` + `gateway/platforms/telegram.py +6` + 2 new tests)
- `05022066 feat(bluebubbles): support group mention gating` —— `gateway/config.py +16` + `gateway/platforms/bluebubbles.py +97` + 132 test

For details, see [[2026-06-02-update#5-gateway-structured-stream-event-protocol]] / [[2026-06-02-update#6-per-platform-streaming-default]] / [[2026-06-02-update#16-telegram-observed-media--reusable-primitive]] / [[2026-06-02-update#17-gateway-extract-strip-recover]].

---

## Related pages
- [[Session Search And Sessiondb|session-search-and-sessiondb]]

- [Gateway Session Management](gateway-session-management.md) — Gateway session management architecture
- [Cron Scheduling](cron-scheduling.md) — Cron scheduler driven by gateway
- [Hook System Architecture](hook-system-architecture.md) — Gateway event hook system
- [Security Defense System](security-defense-system.md) — Webhook hardening, Gateway platform approval authorization chain, WeCom callback defusedxml, API server key placeholder
- [Dashboard Auth Oauth Gate](dashboard-auth-oauth-gate.md) — Dashboard authentication independent gate (complementary with api_server Bearer scheme)

## Related documents

- `gateway/run.py` — Main loop and message distribution
- `gateway/session.py` — SessionStore
- `gateway/platforms/base.py` — platform base class (`extract_local_files`, `SUPPORTED_DOCUMENT_TYPES`, `send_document`, **NEW 2026-06-02** `cache_media_bytes` platform-independent media caching primitive + `supports_draft_streaming`/`render_message_event`/`format_tool_event` three stream-event rendering hooks)
- `gateway/stream_events.py` — **NEW 2026-06-02** 7 frozen dataclasses (MessageChunk/MessageStop/Commentary/ToolCallChunk/ToolCallFinished/LongToolHint/GatewayNotice), 171 lines
- `gateway/stream_dispatch.py` — **NEW 2026-06-02** `GatewayEventDispatcher` routes typed events to adapter render hooks, line 132
- `gateway/delivery.py` — Message delivery (including 2026-05-26 `_looks_like_telegram_private_chat_id` DM topic direct branch)
- `gateway/config.py` — Gateway configuration
- `gateway/platforms/` — platform adapter directory
- `gateway/platforms/api_server.py` — **2026-05-27** Session CRUD + GET /v1/skills + /v1/toolsets (+476 lines)
- `gateway/platforms/wecom_callback.py:20-24` — **NEW 2026-05-26** defusedxml + `DEFUSEDXML_AVAILABLE` flag
- `hermes_cli/gateway.py` — Gateway CLI command
