# graceful shutdown

- 优雅退出
- 监听 `os.signals.SIGINT, SIGTERM` 退出信号, 在退出时做清理工作

## 原理

- https://cloud.tencent.com/developer/article/2301220
- 操作系统 OS 层面: 提供了 `kill -9 （SIGKILL）`和 `kill -15（SIGTERM）` 两种停机策略.
- `SIGKILL` 信号是一个不能被阻塞、处理或忽略的信号，它会立即终止目标进程.
- `SIGTERM` 信号是一个可以被阻塞、处理或忽略的信号，它也可以通知目标进程终止，但是它相对于 SIGKILL 信号来说更加温和，目标进程可以在接收到 SIGTERM 信号时进行一些清理操作，例如保存数据、关闭文件、释放资源等，然后再终止进程

> Docker 处理机制

- 在 Docker 中，执行 docker stop 命令时，它会向容器中的主进程 (pid=1)发送 SIGTERM 信号.
- 如果容器中的进程不响应 SIGTERM 信号，Docker 会等待一定的时间（默认为 10 秒），然后向容器中的所有进程发送 SIGKILL 信号，以强制结束容器中的进程.
- 如果我们需要修改 SIGTERM 信号等待的时间，可以在 docker run 命令中使用 --stop-timeout 参数来更改默认的停止超时时间(单位: s)

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

- https://github.com/topics/graceful-shutdown?o=desc&s=

### docker

> 进程管理

- ✅ [tini](https://github.com/krallin/tini): 搭配 docker 使用, 首选
- ✅ [dumb-init](https://github.com/Yelp/dumb-init)

> web ui 管理工具

- https://github.com/portainer/portainer
- https://github.com/dyrector-io/dyrectorio
- https://github.com/SelfhostedPro/Yacht

### python

- https://github.com/aliev/aioshutdown
    - 支持异步 `aio + graceful shutdown`
- https://github.com/zifter/graceful-shutdown-py
- https://github.com/wbenny/python-graceful-shutdown/tree/master

### rust

- https://github.com/cloudflare/shellflip
    - cloudflare 开发, 高质量库

### golang

- https://juejin.cn/post/6854573220810391560
- https://blog.wu-boy.com/2020/02/what-is-graceful-shutdown-in-golang/
- https://dev.to/antonkuklin/golang-graceful-shutdown-3n6d


