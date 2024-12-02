import flet as ft

from core.views import home_view, HomeView
from core.views import store_view
from core.views import todo_view


def main(page: ft.Page):
    page.title = "Flet Template"

    #
    # register router:
    #
    def route_change(route):
        page.views.clear()
        page.views.append(
            home_view(page),
        )

        # register route:
        if page.route == "/store":
            page.views.append(store_view(page))

        if page.route == "/home":
            page.views.append(HomeView(page))
        if page.route == "/todo":
            page.views.append(todo_view(page))

        #
        #
        #
        page.update()

    #
    # route change:
    #
    page.on_route_change = route_change
    page.go(page.route)
    page.update()


ft.app(main, port=8000, view=ft.AppView.WEB_BROWSER)
