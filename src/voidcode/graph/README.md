# `voidcode.graph`

这里是 VoidCode 的执行编排层。

## 定位

`voidcode.graph` 负责描述和驱动具体的执行循环，例如确定性只读循环或后续更真实的 agent execution engine。它关注步骤如何推进，而不是产品级治理如何统一。

## 负责什么

- 执行循环与步骤推进逻辑
- graph/request/response 级别的编排契约
- engine 内部的状态流转

## 不负责什么

- 运行时配置优先级
- 权限、审批与 hooks 管理
- 本地持久化与会话恢复真相
- 客户端传输与 UI 语义

## 边界关系

`voidcode.runtime` 负责选择和调用 graph，并为 graph 提供 resolved config、session state、tool metadata 和执行治理。graph 不应反向成为系统控制面。

## 当前状态

当前这里仍以确定性执行切片为主，是 runtime 驱动下的编排层，而不是独立产品边界。
