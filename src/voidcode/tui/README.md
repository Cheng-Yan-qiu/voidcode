# `voidcode.tui`

这里是 VoidCode 的终端客户端层。

## 定位

`voidcode.tui` 是 runtime 的消费者，用来承载终端交互界面与渲染逻辑。

## 负责什么

- TUI 应用壳层
- 消息与屏幕渲染
- 面向终端用户的交互流

## 不负责什么

- 直接执行工具
- 会话真相存储
- 执行治理、权限和恢复控制面

## 边界关系

TUI 应持续通过 `voidcode.runtime` 暴露的 session、event 和 approval 语义工作，而不是形成独立执行路径。

## 当前状态

TUI 仍然是较早期的客户端层，优先级低于当前的 CLI 与 Web 主路径。
