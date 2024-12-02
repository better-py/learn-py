import flet as ft


def home_view(page: ft.Page):
    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings")
    ]

    return ft.View(
        "/",

        [

            ft.Row([
                ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ft.ElevatedButton("Visit Home", on_click=lambda _: page.go("/home")),
                ft.ElevatedButton("Visit Todo", on_click=lambda _: page.go("/todo")),
            ])

        ],

        appbar=ft.AppBar(
            leading=ft.Icon(ft.Icons.ROCKET),
            leading_width=100,
            title=ft.Text("Home View", size=32, text_align="start"),
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


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]

        self.route = "/"

        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.ROCKET),
            leading_width=100,
            title=ft.Text("Home View 2", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )

    def build(self):
        return ft.Container(
            ft.SafeArea(
                ft.Card(
                    ft.Column(
                        [
                            ft.Row([
                                ft.ElevatedButton("Visit Store", on_click=lambda _: self.page.go("/store")),
                                ft.ElevatedButton("Visit Home", on_click=lambda _: self.page.go("/home")),
                                ft.ElevatedButton("Visit Todo", on_click=lambda _: self.page.go("/todo")),
                            ]),

                            ft.ListView(
                                [
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BUILD), title=ft.Text("test1")),
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BOOK), title=ft.Text("test2")),
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BADGE), title=ft.Text("test3")),
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BOY), title=ft.Text("test4")),
                                ],
                                padding=10,
                            ),

                            ft.ListView(
                                [
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BUILD), title=ft.Text("list2")),
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BOOK), title=ft.Text("list2")),
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BADGE), title=ft.Text("list2")),
                                    ft.ListTile(trailing=ft.Icon(ft.Icons.BOY), title=ft.Text("list2")),
                                ],
                                padding=10,
                            ),
                        ]
                    ),
                ), expand=True,
            )
        )
