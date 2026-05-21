---
title: CLI 架构与终端交互设计
created: 2026-04-07
updated: 2026-04-11
type: concept
tags: [architecture, cli, terminal, ux]
sources: [hermes-agent 源码分析 2026-04-07]
---

# CLI 架构与终端交互设计

## 设计原理

Hermes CLI 提供完整的终端用户体验：自动补全、多行编辑、流式输出、工具调用可视化。基于 `prompt_toolkit` 和 `rich` 构建。

## 核心组件

```python
# cli.py
class HermesCLI:
    """Hermes CLI 主类"""
    
    def __init__(self):
        self.agent = None
        self.config = load_cli_config()
        self.session_db = SessionDB(...)
        self.todo_store = TodoStore()
    
    def run(self):
        """主循环"""
        while True:
            user_input = self._get_input()  # prompt_toolkit 输入
            if user_input.startswith("/"):
                self._handle_command(user_input)
            else:
                self._handle_message(user_input)
```

## 输入系统

```python
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

session = PromptSession(
    history=FileHistory("~/.hermes/input_history"),
    auto_suggest=AutoSuggestFromHistory(),
    completer=SlashCommandCompleter(),  # 定义在 hermes_cli/commands.py
)

user_input = session.prompt(get_active_prompt_symbol())  # 提示符号通过 skin engine 配置
```

### 斜杠命令补全

```python
class SlashCommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text = document.text_before_cursor
        if text.startswith("/"):
            for cmd_name, cmd_def in COMMANDS.items():
                if cmd_name.startswith(text[1:]):
                    yield Completion(cmd_name, start_position=-len(text[1:]))
```

## 显示系统

### KawaiiSpinner

```python
# agent/display.py
class KawaiiSpinner:
    """动画加载指示器"""
    
    SPINNERS: dict          # 9 种命名动画集 ('dots', 'bounce', 'grow', ...)
    KAWAII_WAITING: list     # 10 个多字符颜文字
    KAWAII_THINKING: list    # 15 个多字符颜文字
    THINKING_VERBS: list    # 15 个动词 ("pondering", "contemplating", "musing", "cogitating", "ruminating", ...)
    
    def show(self, message: str):
        """显示加载动画"""
        # 使用 Rich 面板和动画
```

### 工具调用预览

```python
def build_tool_preview(tool_name: str, args: dict) -> str:
    """构建工具调用预览"""
    preview = f"🔧 {tool_name}("
    for key, value in list(args.items())[:3]:
        preview += f"\n  {key}={preview_value(value)},"
    preview += "\n)"
    return preview

def get_cute_tool_message(tool_name: str) -> str:
    """获取可爱的工具执行消息"""
    emoji = _get_tool_emoji(tool_name)
    return f"{emoji} Calling {tool_name}..."
```

## Skin 引擎

```python
# hermes_cli/skin_engine.py
@dataclass
class SkinConfig:
    """皮肤配置数据类"""
    ...

# 模块级函数（非类）
def init_skin_from_config(): ...
def get_active_skin() -> SkinConfig: ...
def list_skins() -> list: ...
def set_active_skin(name: str): ...

# 配置示例
# ~/.hermes/config.yaml
display:
  skin: "default"  # 或自定义皮肤名称
```

## 优越性分析

### 与其他 Agent 框架对比

| 特性 | Hermes | Claude Code | Codex CLI |
|------|--------|-------------|-----------|
| 斜杠命令补全 | ✅ 自动 | ✅ | ❌ |
| 多行编辑 | ✅ | ✅ | ✅ |
| 输入历史 | ✅ 文件持久化 | ✅ | ✅ |
| 动画加载 | ✅ KawaiiSpinner | ✅ 简单 | ✅ 简单 |
| 主题系统 | ✅ Skin Engine | ❌ | ❌ |
| 工具调用预览 | ✅ 格式化 | ✅ | ❌ |

## v0.12 - v0.14 新增子命令与斜杠命令

### 新 hermes 子命令

| 命令 | 引入版本 | 说明 |
|------|---------|------|
| `hermes -z <prompt>` | v0.12.0 | One-shot 非交互模式，配 `--model` / `--provider` / `HERMES_INFERENCE_MODEL` |
| `hermes update --check` | v0.12.0 | preflight 升级检查 + opt-in HERMES_HOME backup |
| `hermes curator {archive, prune, list-archived, backup, rollback}` | v0.12/v0.13 | Curator 扩展子命令（详见 [[skills-system-architecture]]） |
| `hermes kanban {add, dispatch, claim, complete, reclaim, ...}` | v0.13.0 | 持久化 Kanban CLI（详见 [[multi-agent-architecture]]） |
| `hermes proxy {start, status, list-providers}` | v0.14.0 | OpenAI-compatible 本地代理：`hermes_cli/proxy/cli.py:30,78,102` |
| `hermes acp --setup-browser` | v0.14.0 | Zed ACP registry 引导浏览器工具安装 |
| `pip install hermes-agent && hermes` | v0.14.0 | PyPI 正式上架（`pyproject.toml:6` `name = "hermes-agent"`） |

### 新斜杠命令（v0.13.0+）

`hermes_cli/commands.py`：

| 斜杠 | 位置 | 说明 |
|------|------|------|
| `/goal <目标>` | `commands.py:105` | 锁定跨轮持久目标（Ralph loop），judge 评分推进直到 DONE（`hermes_cli/goals.py`） |
| `/subgoal {show, append, remove, clear}` | `commands.py:107` | 给运行中的 `/goal` mid-loop 追加成功标准 |
| `/handoff <profile>` | `commands.py:82` | 实时迁移整个 session（v0.14.0 升级带 message + tool call + context 一起迁） |
| `/steer <text>` | `commands.py:103` | 对正在运行的 agent 注入纠偏指令 |
| `/queue <text>` | `commands.py:101` | 后续指令排队进 inflight agent |
| `/reload-skills` | v0.12.0 | rescan `~/.hermes/skills/`（不打破 prompt cache） |
| `/reload` | v0.12.0 | `.env` 热重载（TUI 也支持） |
| `/mouse` | v0.12.0 | toggle ConPTY phantom mouse 注入 |

## Native Windows 支持（v0.14.0+）

`scripts/check-windows-footguns.py` + `pyproject.toml:60,66`（tzdata、psutil）：原生 `cmd.exe` + PowerShell 跑通，**无需 WSL**。完整 PowerShell installer 含 MinGit 自动安装、Microsoft Store python stub 检测、前台 Ctrl+C dance。本版后续跟 40+ Windows-only fix（taskkill、native PTY、信号差异、路径规范化、file-locking）。

## OSC8 可点击 URL（v0.14.0+）

任何支持 OSC8 的终端中 agent 输出的 URL 都是真 hyperlink，hover 高亮、点击在浏览器打开。iTerm2 / Kitty / Ghostty / 现代 Windows Terminal 都支持。

## 国际化（v0.13.0+）

`locales/` 共 **16 个语言 YAML**（af、de、en、es、fr、ga、hu、it、ja、ko、pt、ru、tr、uk、zh、zh-hant），gateway + CLI 静态消息可翻译。Docs 站点拿 zh-Hans。

## 相关页面

- [[configuration-and-profiles]] — 配置管理与 Profile 系统
- [[hook-system-architecture]] — Hook 与插件扩展系统
- [[session-search-and-sessiondb]] — 会话搜索与 SessionDB
- [[voice-mode-architecture]] — 语音模式（Push-to-talk → STT → TTS）
- [[skin-engine]] — 皮肤/主题自定义
- [[context-references]] — @file/@diff/@url 引用系统
- [[worktree-isolation]] — Git Worktree 并行隔离
- [[code-execution-sandbox]] — 代码执行沙箱
- [[multi-agent-architecture]] — `/goal`、`/handoff`、`/steer`、`/queue`、Kanban CLI
- [[smart-model-routing]] — `hermes proxy` OpenAI-compatible 本地代理

## 相关文件

- `cli.py` — CLI 主类
- `hermes_cli/main.py` — 入口点和子命令
- `hermes_cli/commands.py` — 斜杠命令定义（lines 82, 101, 103, 105, 107 为新增）
- `hermes_cli/goals.py` — `/goal` Ralph loop 实现
- `hermes_cli/kanban.py` — Kanban CLI（2677 行）
- `hermes_cli/proxy/` — OpenAI-compatible 本地代理（v0.14.0+）
- `hermes_cli/dump.py` — `hermes dump` 环境摘要（纯文本，用于调试/提 issue）
- `agent/display.py` — 显示系统
- `hermes_cli/skin_engine.py` — 皮肤引擎
- `locales/` — 16 个语言 YAML
