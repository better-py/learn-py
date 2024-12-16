from typing import Sequence

import flet as ft
import flet_easy as fs


def layout_view(data: fs.Datasy, title: str = None, controls: Sequence[ft.Control] | None = None, **kwargs) -> ft.View:
    drawer = ft.NavigationDrawer(
        open=True,
        visible=True,
        selected_index=1,
        controls=[

            ft.CircleAvatar(
                content=ft.Text("Henry"),
                width=200,
            ),

            ft.Divider(thickness=1),

            # ft.ListView(controls=[], padding=10, ),

            # menu
            ft.ListTile(
                leading=ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE, size=30),
                title=ft.Text("Home"),
                on_click=data.go("/"),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.NOTES, color=ft.Colors.ORANGE, size=30),
                title=ft.Text("Todo"),
                on_click=data.go("/todo"),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.CALCULATE, color=ft.Colors.GREEN, size=30),
                title=ft.Text("Counter"),
                on_click=data.go("/counter"),
            ),

            ft.ListTile(
                leading=ft.Icon(ft.Icons.STORE, color=ft.Colors.RED, size=30),
                title=ft.Text("Store"),
                on_click=data.go("/store"),
            ),

            ft.ListTile(
                leading=ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.ORANGE, size=30),
                title=ft.Text("Settings"),
                on_click=data.go("/settings"),
            ),

            ft.ListTile(
                leading=ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.ORANGE, size=30),
                title=ft.Text("About"),
                on_click=data.go("/about"),
            ),
        ],
    )

    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings")
    ]

    appbar = ft.AppBar(
        leading=ft.IconButton(icon=ft.icons.MENU, on_click=lambda _: data.page.open(drawer)),
        title=ft.Text(title if title else "Home View", size=24, text_align="start"),
        center_title=False,
        # toolbar_height=75,
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

    return ft.View(
        "/",

        # controls
        controls=controls if controls else [
            ft.Row([
                ft.ElevatedButton("Visit Store", on_click=data.go("/store")),
                ft.ElevatedButton("Visit Home", on_click=data.go("/")),
                ft.ElevatedButton("Visit Todo", on_click=data.go("/todo")),
                ft.ElevatedButton("Visit Counter", on_click=data.go("/counter")),
            ])

        ],

        # drawer
        drawer=drawer,

        # appbar
        appbar=appbar,
        **kwargs,
    )
