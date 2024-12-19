import flet as ft
import flet_easy as fs

from app.core import app
from app.layout import layout_view


# We add a page
@app.page(route="/flet-easy", title="Flet-Easy")
def index_page(data: fs.Datasy):
    return ft.View(
        controls=[
            ft.Text("Home page"),
            ft.FilledButton("Go to Counter", on_click=data.go("/counter")),
        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )


@app.page(route="/")
@app.page(route="/home")
def home_view(data: fs.Datasy):
    return layout_view(
        data,
        controls=[
            ft.Container(
                ft.SafeArea(
                    ft.Card(
                        ft.Column(
                            [

                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Store",
                                            on_click=lambda _: data.page.go("/store"),
                                        ),
                                        ft.ElevatedButton(
                                            "Home",
                                            on_click=lambda _: data.page.go("/home"),
                                        ),
                                        ft.ElevatedButton(
                                            "Todo",
                                            on_click=lambda _: data.page.go("/todo"),
                                        ),
                                        ft.ElevatedButton(
                                            "Counter",
                                            on_click=lambda _: data.page.go("/counter"),
                                        ),
                                    ]
                                ),
                                ft.ListView(
                                    [
                                        ft.ListTile(
                                            trailing=ft.Icon(ft.Icons.BUILD),
                                            title=ft.Text("list2"),
                                        ),
                                        ft.ListTile(
                                            trailing=ft.Icon(ft.Icons.BOOK),
                                            title=ft.Text("list2"),
                                        ),
                                        ft.ListTile(
                                            trailing=ft.Icon(ft.Icons.BADGE),
                                            title=ft.Text("list2"),
                                        ),
                                        ft.ListTile(
                                            trailing=ft.Icon(ft.Icons.BOY),
                                            title=ft.Text("list2"),
                                        ),
                                    ],
                                    padding=10,
                                ),
                            ]
                        ),
                    ),
                    expand=True,
                )
            )
        ],
    )
