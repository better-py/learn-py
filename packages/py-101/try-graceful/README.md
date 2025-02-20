# graceful shutdown

- 优雅退出
- 监听 `os.signals.SIGINT, SIGTERM` 退出信号, 在退出时做清理工作

## 解决问题

- 避免代码进程被 `强制 kill` 掉时, 程序出现不一致. (程序外, 被终止运行)

## 应用场景

1. 代码内做了 graceful shutdown 设计, 监听退出信号, 方便做退出时的清理工作, 避免出现运行不一致现象.
2. 配合 docker 部署应用, 可以在外部 `docker stop` 退出应用, 然后对 启动的服务实例, 进行安全管理.

### 真实应用场景

1. 量化交易程序,通常主体是个 `while True` 死循环, 无法对外部的主动退出, 做良好的响应.
2. 常规可选方案是在 `死循环`内部, 定时轮询 redis 退出信号状态位, 或者是 订阅 `消息队列` 的 `exit topic` 来监听.
3. 两种方案, 都不太适合 `高频量化场景(增加延迟)`.
4. 那么就很适合基于 graceful shutdown + docker stop 机制来实现主动退出. (低成本 + 易于实现)

## reference

> golang

- https://juejin.cn/post/6854573220810391560
- https://blog.wu-boy.com/2020/02/what-is-graceful-shutdown-in-golang/
- https://dev.to/antonkuklin/golang-graceful-shutdown-3n6d