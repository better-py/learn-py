import flet as ft
import flet_easy as fs


def home_widget(data: fs.Datasy):
    print("data: ", data.__dict__)

    return ft.Container(
        ft.SafeArea(ft.Card(ft.Column([
            ft.Row([
                ft.ElevatedButton("Store", on_click=data.go("/store")),
                ft.ElevatedButton("Home", on_click=data.go("/home")),
                ft.ElevatedButton("Todo", on_click=lambda _: data.page.go("/todo")),
                ft.ElevatedButton("Counter", on_click=lambda _: data.page.go("/counter")),
            ]),

            ft.ListView([
                ft.ListTile(trailing=ft.Icon(ft.Icons.BUILD),
                            title=ft.Text("list2")),
                ft.ListTile(trailing=ft.Icon(ft.Icons.BOOK),
                            title=ft.Text("list2")),
                ft.ListTile(trailing=ft.Icon(ft.Icons.BADGE),
                            title=ft.Text("list2")),
                ft.ListTile(trailing=ft.Icon(ft.Icons.BOY),
                            title=ft.Text("list2")),
            ]),
        ]), )))
