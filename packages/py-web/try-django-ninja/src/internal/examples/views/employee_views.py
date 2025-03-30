from ninja import Router
from ninja_crud import views, viewsets

from internal.examples.models import Employee
from internal.examples.schemas import EmployeeIn, EmployeeOut


router = Router()


class EmployeeViewSet(viewsets.APIViewSet):
    model = Employee

    read_employee = views.ReadView(response_body=EmployeeOut)
    update_employee = views.UpdateView(
        request_body=EmployeeIn, response_body=EmployeeOut
    )
    delete_employee = views.DeleteView()


EmployeeViewSet.add_views_to(router)
