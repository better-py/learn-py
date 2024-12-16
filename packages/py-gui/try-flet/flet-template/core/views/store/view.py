import flet as ft
import flet_easy as fs

from core.app import app


@app.page('/store')
def store_view(data: fs.Datasy):
    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings")
    ]

    return ft.View(
        "/store",

        [
            ft.Row([
                ft.ElevatedButton("Visit Store", on_click=data.go("/store")),
                ft.ElevatedButton("Visit Home", on_click=data.go("/")),
                ft.ElevatedButton("Visit Todo", on_click=data.go("/todo")),
            ])

        ],

        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.STORE),
            leading_width=100,
            title=ft.Text("Store View", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
    )
