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

## 项目列表：

- ✅️ monorepo: [packages](./packages/)
    - [rye](https://arc.net/l/quote/nfjcylkn) now suppport [workspace](https://rye-up.com/guide/workspaces/)

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
| ✅️ [xxx]()                              | xxx      | xxx  |

### 🕷️ [Python 爬虫](./packages/py-crawler)

| 项目名称                                                  | 项目描述  | 说明       |  
|:------------------------------------------------------|:------|:---------|
| ✅️ [selenium](./packages/py-crawler/try-selenium)     | 无头浏览器 | 🌟🌟🌟🌟 |
| ✅️ [playwright](./packages/py-crawler/try-playwright) | 无头浏览器 | 🌟🌟🌟   | 
| ✅️ [jieba](./packages/py-try/try-jieba)               | 中文分词库 | 🌟🌟🌟🌟 |

### 💻 [Python GUI](./packages/py-gui)

| 项目名称                                        | 项目描述                                        | 说明       |  
|:--------------------------------------------|:--------------------------------------------|:---------|
| ✅️ [kivy](./packages/py-gui/try-kivy)       | 原生, 跨平台(Windows/macOS/Linux/iOS/Android) 方案 | 🌟🌟🌟🌟 |
| ✅️ [beeware](./packages/py-gui/try-beeware) | 原生, 跨平台(Windows/macOS/Linux/iOS/Android) 方案 | 🌟🌟🌟   |
| ✅️ [py-wry]()                               | 基于 `Tauri/Wry` 的 WebView 方案                 | 🌟🌟🌟🌟 |
| ✅️ [flet](./packages/py-gui/try-flet)       | 基于 `Flutter` 的 GUI 方案                       | 🌟🌟🌟   |
| ✅️ [pyside](./packages/py-gui/try-pyside)   | 基于 `Qt` 的 GUI 方案                            | 🌟🌟     |
| ✅️ [xxx]()                                  | xxx                                         | xxx      |
| ✅️ [xxx]()                                  | xxx                                         | xxx      |    

## Development

> requirements:

- ✅️ python3.10+: 推荐 `python 3.12+`
- ✅ [rye](https://github.com/astral-sh/rye): 包管理工具
    - ❌ [poetry](https://python-poetry.org/docs/) or [PDM](https://pdm-project.org/latest/)
    - 默认不再使用 poetry, 虽然也是支持 poetry 装包的
- ✅️ pyenv: python 版本管理
- ✅️ [go-task](https://taskfile.dev/#/installation): 运行脚本

```bash

# 查看所有项目的运行脚本:
task --list-all

```

> run scripts:

- ✅️ [Taskfile.yml](./Taskfile.yml): 包含所有的项目启动脚本

