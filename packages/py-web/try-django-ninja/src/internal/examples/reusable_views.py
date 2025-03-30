from typing import Any
from uuid import UUID

from django.db import models
from django.http import HttpRequest
from ninja.constants import NOT_SET
from ninja_crud.views import APIView


class ReusableReadView(APIView):
    def __init__(
        self, response_schema: Any = NOT_SET, model: type[models.Model] | None = None
    ) -> None:
        super().__init__(
            "read_reusable",
            methods=["GET"],
            path="/{id}/reusable",
            response_status=200,
            response_body=response_schema,
        )
        self.model = model

    def handler(self, request: HttpRequest, id: UUID) -> models.Model:
        return self.model.objects.get(id=id)


class ReusableAsyncReadView(APIView):
    def __init__(
        self, response_schema: Any = NOT_SET, model: type[models.Model] | None = None
    ) -> None:
        super().__init__(
            "async_read_reusable",
            path="/{id}/reusable/async",
            methods=["GET"],
            response_status=200,
            response_body=response_schema,
        )
        self.model = model

    async def handler(self, request: HttpRequest, id: UUID) -> models.Model:
        return await self.model.objects.aget(id=id)
