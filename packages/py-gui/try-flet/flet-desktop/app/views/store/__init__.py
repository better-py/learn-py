import flet as ft
import flet_easy as fs

from app.core import app
from app.layout import layout_view


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
