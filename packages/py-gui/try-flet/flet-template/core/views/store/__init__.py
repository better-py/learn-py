import flet as ft
import flet_easy as fs

from core.app import app
from core.layout import layout_view


@app.page('/store')
def store_view(data: fs.Datasy):
    return layout_view(data, title="Store", controls=[
        ft.SafeArea(
            ft.Card(
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Text("Store View"),
                    padding=10,
                )
            )
        ),
    ])
