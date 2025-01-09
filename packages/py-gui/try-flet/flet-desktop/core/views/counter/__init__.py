import flet as ft
import flet_easy as fs

from core.app import app
from core.layout import layout_view


# We add a second page
@app.page(route="/counter", title="Counter")
def counter_page(data: fs.Datasy):
    page = data.page

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    return layout_view(
        data,
        title="Counter",
        controls=[
            ft.Row(
                [
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ],
                alignment="center",
            ),

            ft.IconButton(ft.Icons.HOME, on_click=data.go("/home"), icon_color=ft.Colors.GREEN),

        ],
        vertical_alignment="center",
        horizontal_alignment="center",
    )
