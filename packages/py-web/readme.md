# Python Web 框架

- ✅ `Django` YYDS!!! (糊 CMS 和 内网 admin)
- ✅ `Django Ninja` YYDS!!! (糊 API)

## 💡 为什么首选是 Django, 不是 FastAPI?

- ✅ 可以但没必要.
- ✅ 性能讨论口水:
  - Python 性能天花板本就很低, 谈性谁能更好, 也多余.(矮个子里拔将军, 无聊)
  - 与其局限在 Python 上优化性能, 都不如业务做大后, 用 Go 重写来的实际:
    - Go: 在座的各位, 都是垃圾👎🏻!!!
  - 另外, 把 FastAPI 各种插件集成到和 Django 一个等级, 性能也会掉到一档.(五十步笑百步)
- ✅ 生态+易用性+开发效率:
  - 既然已经用了 python, 就不太在意性能, 而更在意易用性.(更快糊项目, 仅此!!!)
  - Django 的生态完备度(丰富度/可靠性/质量)吊打其他所有.

## 🥇 Django

- [Django 中文文档](https://docs.djangoproject.com/zh-hans/)
- <https://github.com/wsvincent/awesome-django>

> 应用场景:

- ✅ 特别适合:
  - 中小型项目
  - 内部cms
  - demo 演示类, 生命周期短(活不过几个月的项目)
  - 初创公司, 原型阶段, 快速 rush 需求, 适应快速变更. (做大之后,用 `go/rust` 等重写)
- ✅ 用法建议:
  - 除了糊 cms, 内网 admin, 可以直接用 django.
  - 快速糊 API, 请用 `Django Ninja`(替代 `Django REST framework`).

> 扩展:

- [Django Ninja](https://django-ninja.dev/)
- [Django REST framework 中文文档](https://www.django-rest-framework.org.cn/)

### 🚀 Django Ninja + CRUD

- ✅ <https://github.com/vitalik/django-ninja>
  - [Django Ninja 中文文档](https://django-ninja.cn/)
  - <https://django-ninja.cn/tutorial/>
- ✅ 首选, 更好. 不再建议使用 `Django REST framework`

#### Django Ninja 扩展

- ✅ <https://github.com/hbakri/django-ninja-crud>
  - [Django Ninja CRUD](https://django-ninja.cn/django-ninja-crud/guides/01-Introduction/)
- ✅ [Django Ninja Extra](https://django-ninja.cn/django-ninja-extra/)
- ✅ [Django Ninja JWT](https://django-ninja.cn/django-ninja-jwt/)

### 🙅🏻 Django REST framework

- 🙅🏻 不建议使用. 请使用 `Django Ninja`
- <https://github.com/encode/django-rest-framework>

## 🥈 FastAPI

- [FastAPI 中文文档](https://fastapi.tiangolo.com/zh/)
- ✅ 虽然FastAPI 很好, 但是, `Django Ninja` 对于熟悉 Django 的人来说, 可能才是首选.

## 🙅🏻 其他(都不建议直接使用)

> 统统不推荐新项目使用

- flask
- tornado
- sanic: 异步
- aiohttp: 异步
- starlette: 异步

## References

- <https://django-ninja.dev/>

> 讨论:

- <https://www.v2ex.com/t/1121609>
- <https://zhuanlan.zhihu.com/p/706929518>
- <https://www.zhihu.com/tardis/zm/art/701628536>
- <https://zhuanlan.zhihu.com/p/714036082>
