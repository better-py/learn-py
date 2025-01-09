import flet as ft
import flet_easy as fs

from app.core import app
from app.layout import layout_view


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
    return layout_view(
        data,
        title="Todo",
        controls=[
            ft.Row([
                ft.ElevatedButton("Store", on_click=data.go("/store")),
                ft.ElevatedButton("Home", on_click=data.go("/home")),
                ft.ElevatedButton("Todo", on_click=data.go("/todo")),
                ft.ElevatedButton("Counter", on_click=data.go("/counter")),
            ]),

            ft.Divider(thickness=1),

            ft.Card(

                ft.Container(
                    alignment=ft.alignment.center,
                    content=TodoApp(),
                    padding=10,
                ),
                margin=10,
                expand=True,

            )

        ]
    )
