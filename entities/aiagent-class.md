# AIAgent Class

> Core dialogue loop class managing LLM interactions and tool calls

## Overview

The `AIAgent` class is the heart of Hermes Agent's conversation loop:
- Message handling and routing
- Tool invocation and result processing
- State management (session, memory)
- Context assembly

## Key Methods

- `run_turn()` - Execute a single conversation turn
- `call_tool()` - Invoke a tool with arguments
- `assemble_prompt()` - Build the LLM prompt
- `update_memory()` - Update persistent memory

## References

- [[agent-loop-and-prompt-assembly]]
- [[memory-system-architecture]]