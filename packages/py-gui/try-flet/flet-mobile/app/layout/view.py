import flet as ft


def view_layout(self, content: ft.Control | None = None) -> ft.Control:
    return ft.Container(
        ft.SafeArea(
            content if content else ft.Column(
                [
                    ft.Text("Hello World"),
                ]
            ),
        ),
        alignment=ft.alignment.center,
        padding=10,
        expand=True,
    )
