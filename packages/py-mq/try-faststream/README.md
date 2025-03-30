# try-faststream

## Description

- 支持 `1:多`: 发 1 条, 多 worker 重复处理.
- 支持 `1:1`: 发 1 条, 单 worker 唯一处理(防止重复消费)
- 支持 `kv` watch: 监听 `kv` 存储的 `key`, 触发 `1:多` 处理.
- 支持 `pull stream`: batch 拉取 `stream` 到本地, 触发 `1:多` 处理.

## Requirements

### 定时任务

> Taskiq 定时任务:

- <https://github.com/taskiq-python/taskiq>
  - <https://taskiq-python.github.io/>
  - <https://pypi.org/project/taskiq-nats/>
  - <https://pypi.org/project/taskiq-redis/>
- 定时任务: <https://taskiq-python.github.io/guide/scheduling-tasks.html>
- 集成: <https://taskiq-python.github.io/framework_integrations/faststream.html>

> rocketry:

- <https://rocketry.readthedocs.io/en/stable/tutorial/basic.html>
- 不活跃, 近 1 年未修复 bug. 有部分依赖 Pydantic v2 有冲突.
- 问题: <https://github.com/Miksus/rocketry/issues/210>
- 替代: <https://github.com/ManiMozaffar/aioclock>
