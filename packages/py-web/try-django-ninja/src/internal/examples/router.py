from ninja import Router

# from .reusable_views import api
from .views import department_router, employee_router


router = Router()

router.add_router("/department", department_router)
router.add_router("/employee", employee_router)


# 注册到 reusable_api
# api.add_router("", router)

__all__ = [
    "router",
]
