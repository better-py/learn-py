"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from routers import api, api_redoc


urlpatterns = [
    path("admin/", admin.site.urls),
    #
    # api
    #   - http://127.0.0.1:8000/api/v1/hello
    #   - http://127.0.0.1:8000/api/v2/hello
    #
    path("api/v1/", api_redoc.urls),  # 注册2套 docs 工具, redoc
    path("api/v2/", api.urls),  # 注册2套 docs 工具, swagger
    #
    # examples
    # path("api/v2/examples/", include(examples_api.urls)),  # 注册 examples
]


DEBUG_TOOLBAR_URLS = [
    path("__debug__/", include("debug_toolbar.urls")),
]

# development + openapi
OPENAPI_URLS: list = []

urlpatterns += DEBUG_TOOLBAR_URLS
urlpatterns += OPENAPI_URLS
