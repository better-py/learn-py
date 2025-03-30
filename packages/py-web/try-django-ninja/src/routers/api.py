import asyncio

from ninja import NinjaAPI, Redoc, Swagger

from internal.examples.router import router as example_router


#
# ref: https://django-ninja.dev/guides/api-docs/
#   - 默认使用 Swagger, 可以改为 Redoc
#   - 同时注册2个 docs 工具方法
#   - 访问:
#       - http://127.0.0.1:8000/api/v1/docs
#       - http://127.0.0.1:8000/api/v2/docs
#
# api = NinjaAPI(docs=Swagger())
api_redoc = NinjaAPI(
    docs=Redoc(), version="v1", urls_namespace="api_redoc"
)  # use Redoc
api = NinjaAPI(docs=Swagger(), version="v2")  # use Redoc


#
# Register routers
#
api.add_router("examples/", example_router)  # 注册 examples
api_redoc.add_router("examples/", example_router)  # 注册 examples


@api_redoc.get("/hello")
@api.get("/hello")
def hello(request):
    return "Hello world"


@api_redoc.get("/say-after")
@api.get("/say-after")
async def say_after(request, delay: int, word: str):
    await asyncio.sleep(delay)
    return {"saying": word}
