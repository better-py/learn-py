# ZeroMQ

> 项目:

- <https://zeromq.org/>
- <<https://github.com/zeromq/>

```ruby

为什么选择 ZeroMQ？

ZeroMQ（也称为 ØMQ、0MQ 或 zmq）看起来像一个可嵌入的网络库，但其作用却像一个并发框架。它为您提供了跨各种传输（如进程内、进程间、TCP 和多播）传输原子消息的套接字。

您可以使用扇出、发布-订阅、任务分配和请求-回复等模式将套接字 N 对 N 连接起来。它的速度足够快，可以作为集群产品的结构。其异步 I/O 模型为您提供了可扩展的多核应用程序，这些应用程序构建为异步消息处理任务。

它拥有大量语言 API，可在大多数操作系统上运行。


多路传输

通过 inproc、IPC、TCP、UDP、TIPC、多播和 WebSocket 传输消息

```

> 特点:

- 轻量级, 高性能, 可扩展.

> python lib:

- [pyzmq](https://pyzmq.readthedocs.io/en/latest/)
- [zerorpc](https://zerorpc.readthedocs.io/en/latest/)

> 适用场景:

- 特别适合高频量化交易, 在进程内实现 mq 通信模式, 低延迟.
