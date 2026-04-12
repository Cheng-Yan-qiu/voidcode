# `voidcode.mcp`

这里是 MCP 能力层的预期目录。

## 定位

`voidcode.mcp` 的目标是承载 MCP 相关的协议模型、配置 schema、server 定义与 capability-layer primitives，为后续 runtime-managed MCP integration 预留清晰边界。

## 负责什么

- MCP 相关 schema 与配置模型
- MCP server / connection definition 的纯数据结构
- 不依赖 runtime session 状态的协议契约
- 可被 runtime 消费的 preset / registry / resolution primitives

## 不负责什么

- 真实连接生命周期管理
- runtime 事件发射
- session 持久化与恢复语义
- 客户端直连 MCP 的执行路径

## 边界关系

如果未来引入 MCP，`voidcode.runtime` 仍应持有 lifecycle、event、session truth 和 capability governance；`voidcode.mcp` 负责提供纯 contract / schema / preset 层。

## 当前状态

这个目录目前是文档与边界占位，还没有真实实现。MCP 现阶段仍属于 design-first、implementation-later 的能力面。
