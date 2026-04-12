# `voidcode.tools`

这里是 VoidCode 的工具能力层。

## 定位

`voidcode.tools` 承载内置工具实现与工具契约，供 runtime 统一注册、暴露和治理。它的目标是提供稳定的能力表面，而不是自己决定运行时策略。

## 负责什么

- 工具契约与参数/返回形状
- 内置工具的具体实现
- 与特定能力相关的最小适配层（例如 LSP tool adapter）

## 不负责什么

- 会话持久化与恢复
- 审批决策
- 客户端交互逻辑
- 独立的 capability lifecycle 管理

## 边界关系

工具通过 runtime 注册和执行，graph 与客户端都不应绕过 runtime 直接管理工具生命周期。工具契约面向 runtime 消费，而不是直接面向 UI。

## 当前状态

这里已经是相对稳定的能力层。后续如果引入更多 capability package，它们通常应通过 runtime 和 tools 的既有边界接入系统。
