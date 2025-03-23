# learn-py

<p align="#middle">
    <a href="https://discord.com/invite/MnDA9pfWAW" target="_blank">
      <img src="https://img.shields.io/badge/Discord-GossipCoder-%237289DA.svg?logo=iscord&logoColor=white" alt="Discord">
    </a>
    <a href="https://discord.com/invite/MnDA9pfWAW" target="_blank">
      <img src="https://img.shields.io/discord/877031318272217179" alt="Discord">
    </a>
    <img src="https://visitor-badge.laobi.icu/badge?page_id=better-py" alt="10000" />
</p>

- python 一些库的调研 & 实践

## 💡 文档

- <https://better-py.github.io/learn-py/>

## 🐞 开发环境

- ✅ python: 3.12+(无需单独安装)
  - 只需要安装 uv, uv 会在项目内创建一个 python 虚拟环境(.venv)
- ✅ python 包管理工具: [uv](https://github.com/astral-sh/uv)
- ✅ 项目构建工具: [go-task](https://github.com/go-task/task)
  - ✅️ [Taskfile.yml](./Taskfile.yml): 包含所有的`子项目`启动脚本

```ruby
# cd git-repo-root-dir
# 安装所有子项目依赖
uv sync --all-packages --upgrade

# or
task sync

```

- ✅ 注意部分项目,需要根据 [.env.local](./.env.local) 创建 .env 文件
- ✅ 运行示例

```ruby
# cd git-repo-root-dir
# 运行示例
task quant:bn:r -- rest/run01_spot.py

# or
uv run packages/py-quant/try-binance/src/rest/run01_spot.py

```

## 🚀 项目列表

- ✅️ monorepo: [packages](./packages/)
  - [uv](https://github.com/astral-sh/uv) now suppport [workspace](https://rye-up.com/guide/workspaces/)
- ✅ 并未列举全部`子项目`, 请自行查看每个`子目录`了解.

[//]: # (y23m01p01-xxx 项目编号规则)

### 💡 [Python 基础](./packages/py-101)

| 项目名称                           | 项目描述        | 说明   |  
|:-------------------------------|:------------|:-----|
| ✅️ [py-101](./packages/py-101) | python 基础示例 | ⭐️⭐️ |

### 🔥 [Python AI/LLM/GPT](./packages/py-ai)

| 项目名称                                         | 项目描述                                                                              | 说明        |  
|:---------------------------------------------|:----------------------------------------------------------------------------------|:----------|
| ✅️ [try-chroma](packages/py-ai/try-chroma)   | [chroma](https://github.com/chroma-core/chroma) 是LLM 常用 `向量数据库`， 调研 & 测试          | ⭐️⭐️⭐️    |
| ✅️ [try-autogpt](packages/py-ai/try-autogpt) | [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) GPT 最火🔥️框架, 调研 & 测试 | ⭐️⭐️⭐⭐️⭐️ |
| ✅️ [xxx]()                                   | xxx                                                                               | xxx       |
| ✅️ [xxx]()                                   | xxx                                                                               | xxx       |

### 📈 [Python Quant](./packages/py-quant)

| 项目名称                                    | 项目描述     | 说明   |  
|:----------------------------------------|:---------|:-----|
| ✅️ [ccxt](./packages/py-quant/try-ccxt) | 数字货币交易框架 | ⭐️⭐️ |
| ✅️ [vnpy](./packages/py-quant/try-vnpy)                                    | vnpy 框架验证         | ⭐️⭐️  |
| ✅️ [hftbacktest](./packages/py-quant/try-hftbacktest)                       | 高频回测框架         | ⭐️⭐️  |
| ✅️ [binance](./packages/py-quant/try-binance)                              | binance 交易所      | ⭐️⭐️  |
| ✅️ [gateio](./packages/py-quant/try-gateio)                                | gateio 交易所       | ⭐️⭐️  |

### 🕷️ [Python 爬虫](./packages/py-crawler)

| 项目名称                                                  | 项目描述  | 说明       |  
|:------------------------------------------------------|:------|:---------|
| ✅️ [selenium](./packages/py-crawler/try-selenium)     | 无头浏览器 | 🌟🌟🌟🌟 |
| ✅️ [playwright](./packages/py-crawler/try-playwright) | 无头浏览器 | 🌟🌟🌟   |
| ✅️ [jieba](./packages/py-try/try-jieba)               | 中文分词库 | 🌟🌟🌟🌟 |

### 💻 [Python GUI](./packages/py-gui)

| 项目名称                                        | 项目描述                                        | 说明         |  
|:--------------------------------------------|:--------------------------------------------|:-----------|
| ✅️ [flet](./packages/py-gui/try-flet)       | 基于 `Flutter` 的 GUI 方案                       | 🌟🌟🌟🌟🌟 |
| ✅️ [kivy](./packages/py-gui/try-kivy)       | 原生, 跨平台(Windows/macOS/Linux/iOS/Android) 方案 | 🌟🌟🌟🌟   |
| ✅️ [beeware](./packages/py-gui/try-beeware) | 原生, 跨平台(Windows/macOS/Linux/iOS/Android) 方案 | 🌟🌟🌟     |
| ✅️ [py-wry]()                               | 基于 `Tauri/Wry` 的 WebView 方案                 | 🌟🌟🌟🌟   |
| ✅️ [pyside](./packages/py-gui/try-pyside)   | 基于 `Qt` 的 GUI 方案                            | 🌟🌟       |
| ✅️ [xxx]()                                  | xxx                                         | xxx        |
| ✅️ [xxx]()                                  | xxx                                         | xxx        |
