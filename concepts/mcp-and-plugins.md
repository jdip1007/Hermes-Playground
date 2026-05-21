---
title: MCP 集成与插件系统
created: 2026-04-07
updated: 2026-04-07
type: concept
tags: [architecture, mcp, plugins, extensibility]
sources: [hermes-agent 源码分析 2026-04-07]
---

# MCP 集成与插件系统

## 设计原理

Hermes 通过 **MCP（Model Context Protocol）** 和**插件系统**实现可扩展性，允许连接外部工具和自定义行为。

## MCP 集成

```python
# tools/mcp_tool.py (~2176 行)

class MCPServerTask:
    """MCP 服务器任务"""
    
    def __init__(self, config: dict):
        self.servers = {}
        self.tools = {}
    
    async def connect_server(self, name: str, config: dict):
        """连接 MCP 服务器"""
        transport = config.get("transport", "stdio")
        
        if transport == "stdio":
            process = await asyncio.create_subprocess_exec(
                *config["command"],
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
            )
            self.servers[name] = {
                "process": process,
                "transport": transport,
            }
        elif transport == "http":
            self.servers[name] = {
                "url": config["url"],
                "transport": transport,
            }
        
        # 获取服务器工具
        tools = await self._list_tools(name)
        for tool in tools:
            self.tools[f"{name}:{tool['name']}"] = tool
    
    async def call_tool(self, tool_name: str, args: dict) -> dict:
        """调用 MCP 工具"""
        server_name, tool_name = tool_name.split(":", 1)
        server = self.servers[server_name]
        
        if server["transport"] == "stdio":
            return await self._call_stdio_tool(server, tool_name, args)
        elif server["transport"] == "http":
            return await self._call_http_tool(server, tool_name, args)
```

### MCP OAuth 支持

```python
# tools/mcp_oauth.py

async def authenticate_mcp_server(server_config: dict) -> dict:
    """MCP 服务器 OAuth 认证"""
    auth_type = server_config.get("auth", {}).get("type")
    
    if auth_type == "oauth":
        # 实现 OAuth 流程
        auth_url = server_config["auth"]["url"]
        client_id = server_config["auth"]["client_id"]
        # ...
        return {"access_token": token, "expires_at": expires}
    
    elif auth_type == "api_key":
        return {"api_key": server_config["auth"]["api_key"]}
    
    return {}
```

## 插件系统

```python
# hermes_cli/plugins.py

class Plugin:
    """插件基类"""
    
    name: str = ""
    version: str = "1.0.0"
    description: str = ""
    
    def on_load(self):
        """插件加载时调用"""
        pass
    
    def on_unload(self):
        """插件卸载时调用"""
        pass

# 钩子系统
_HOOKS = {
    "on_session_start": [],
    "pre_llm_call": [],
    "post_llm_call": [],
    "on_tool_call": [],
    "on_session_end": [],
}

def register_hook(hook_name: str, callback: callable):
    """注册钩子回调"""
    if hook_name in _HOOKS:
        _HOOKS[hook_name].append(callback)

def invoke_hook(hook_name: str, **kwargs) -> list:
    """调用钩子"""
    results = []
    for callback in _HOOKS.get(hook_name, []):
        try:
            result = callback(**kwargs)
            results.append(result)
        except Exception as e:
            logger.warning(f"Hook {hook_name} failed: {e}")
    return results
```

### 内存插件

```python
# plugins/memory/__init__.py

class MemoryPlugin(Plugin):
    """内存插件（Honcho 集成）"""
    
    name = "honcho-memory"
    
    def on_session_start(self, session_id: str, **kwargs):
        """会话开始时预热缓存"""
        self._warm_cache(session_id)
    
    def pre_llm_call(self, user_message: str, **kwargs):
        """LLM 调用前注入上下文"""
        context = self._fetch_context(user_message)
        return {"context": context}
    
    def on_session_end(self, messages: list, **kwargs):
        """会话结束时持久化"""
        self._persist_session(messages)
```

## 插件 CLI

```bash
# 插件管理
hermes plugins list           # 列出已安装插件
hermes plugins install <name> # 安装插件
hermes plugins remove <name>  # 移除插件
hermes plugins update <name>  # 更新插件
```

## 配置

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  filesystem:
      command: ["npx", "-y", "@modelcontextprotocol/server-filesystem", "/root/work"]
    github:
      command: ["npx", "-y", "@modelcontextprotocol/server-github"]
      env:
        GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_TOKEN}"

plugins:
  enabled:
    - honcho-memory
    - custom-plugin
```

## 优越性分析

### 与其他 Agent 框架对比

| 特性 | Hermes | Cursor | Claude Code |
|------|--------|--------|-------------|
| MCP 支持 | ✅ 完整 | ✅ | ✅ |
| MCP OAuth | ✅ | ❌ | ✅ |
| 插件系统 | ✅ 钩子系统 | ❌ | ❌ |
| 自定义工具 | ✅ 注册表 | ❌ | ❌ |
| 插件 CLI | ✅ | N/A | N/A |

## MCP SSE Transport（v0.13.0+）

`tools/mcp_tool.py:5,35,52,203-208`：MCP 服务器现在支持三种 transport：

```yaml
# config.yaml
mcp:
  servers:
    my-sse-server:
      url: http://localhost:8000/sse
      transport: sse       # 替代默认 Streamable HTTP
```

- **SSE transport** 配 `transport: sse`
- **OAuth forwarding** for SSE：MCP server 后端的 OAuth 流可直接转发
- **Stale-pipe retries**：连接断开后自动重连
- **Image result 改作 MEDIA tag**（之前被直接丢弃）
- **Lifecycle keepalive** for 长 lived waits

## `transform_llm_output` 插件 lifecycle Hook（v0.13.0+）

`agent/conversation_loop.py:3936,3944` + `hermes_cli/plugins.py:136`：新增 lifecycle hook，让插件在 LLM 输出**回到对话之前**重塑/过滤。Context-window reducer 和内容过滤器用得上：

```python
def register(ctx):
    @ctx.transform_llm_output
    def shrink_excess(output: str) -> str:
        # 例如：截掉超过 10KB 的部分，加 [truncated] 标记
        return output[:10240] + "\n[...truncated]" if len(output) > 10240 else output
```

## Plugin `ctx.llm` + `tool_override`（v0.14.0+）

插件可走 active provider + credentials **直接发 LLM call**，无需手动 client wiring：

```python
def register(ctx):
    @ctx.register_tool("my_custom_search")
    async def search(query: str) -> str:
        # 走主 agent 同款 provider/model 路由 + 凭证
        return await ctx.llm.complete(f"Search: {query}", model="auto")
```

**`tool_override=True`** flag 允许插件**干净替换**一个 built-in 工具的实现，旧实现自动让位。

## 相关页面

- [[tool-registry-architecture]] — 插件通过 registry.register() 注册工具
- [[hook-system-architecture]] — 插件钩子系统与网关事件钩子互补
- [[model-tools-dispatch]] — MCP 工具通过 discover 机制集成到编排层

## 相关文件

- `tools/mcp_tool.py` — MCP 服务器任务（SSE transport: lines 5,35,52,203-208）
- `tools/mcp_oauth.py` — MCP OAuth
- `hermes_cli/plugins.py` — 插件系统（transform_llm_output: line 136）
- `agent/conversation_loop.py` — transform_llm_output dispatch（lines 3936, 3944）
- `plugins/` — 插件目录
