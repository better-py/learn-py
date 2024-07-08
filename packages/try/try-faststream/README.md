# try-faststream

## Description

- 支持 `1:多`: 发 1 条, 多 worker 重复处理.
- 支持 `1:1`: 发 1 条, 单 worker 唯一处理(防止重复消费)
- 支持 `kv` watch: 监听 `kv` 存储的 `key`, 触发 `1:多` 处理.
- 支持 `pull stream`: batch 拉取 `stream` 到本地, 触发 `1:多` 处理.

## Requirements

- https://taskiq-python.github.io/
- https://pypi.org/project/taskiq-nats/
- https://pypi.org/project/taskiq-redis/