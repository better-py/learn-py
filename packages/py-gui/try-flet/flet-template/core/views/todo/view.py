import flet as ft
import flet_easy as fs

from core.app import app


class TodoApp(ft.Column):
    # application's root control is a Column containing all other controls
    def __init__(self):
        super().__init__()
        self.new_task = ft.TextField(hint_text="What needs to be done?", expand=True)
        self.tasks_view = ft.Column()
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.tasks_view,
        ]

    def add_clicked(self, e):
        self.tasks_view.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


@app.page(route="/todo")
def todo_view(data: fs.Datasy):
    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings")
    ]

    return ft.View(
        "/todo",

        [
            ft.Row([
                ft.ElevatedButton("Visit Store", on_click=data.go("/store")),
                ft.ElevatedButton("Visit Home", on_click=data.go("/home")),
                ft.ElevatedButton("Visit Todo", on_click=data.go("/todo")),
            ]),

            TodoApp(),
        ],

        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.TASK),
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
