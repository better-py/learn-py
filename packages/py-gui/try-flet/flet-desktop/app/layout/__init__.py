from typing import Sequence

import flet as ft
import flet_easy as fs

from app.widgets.home import home_widget


def layout_view(data: fs.Datasy, title: str = None, controls: Sequence[ft.Control] | None = None, **kwargs) -> ft.View:
    drawer = ft.NavigationDrawer(
        open=False,
        visible=True,
        selected_index=1,
        # bgcolor=ft.Colors.PINK_300,
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
                leading=ft.Icon(ft.Icons.INFO, color=ft.Colors.PINK_300, size=30),
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
        leading=ft.IconButton(icon=ft.Icons.MENU, on_click=lambda _: data.page.open(drawer)),
        title=ft.Text(title if title else "Home", size=24, text_align="start"),
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

    rail = ft.NavigationRail(

        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=50,
        min_extended_width=400,
        # leading=ft.FloatingActionButton(
        #     icon=ft.Icons.CREATE, bgcolor=ft.Colors.RED,
        #     on_click=lambda _: data.page.go("/store")),
        # trailing=ft.FloatingActionButton(
        #     icon=ft.Icons.CREATE, bgcolor=ft.Colors.RED,
        #     on_click=lambda _: data.page.go("/counter")),
        # group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.HOME_OUTLINED, color=ft.Colors.BLUE),
                selected_icon=ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE),
                label_content=ft.Text("Home"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.NOTES_OUTLINED, color=ft.Colors.RED),
                selected_icon=ft.Icon(ft.Icons.NOTES, color=ft.Colors.RED),
                label_content=ft.Text("Todo"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.CALCULATE_OUTLINED, color=ft.Colors.GREEN),
                selected_icon=ft.Icon(ft.Icons.CALCULATE, color=ft.Colors.GREEN),
                label_content=ft.Text("Counter"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.STORE_OUTLINED, color=ft.Colors.RED),
                selected_icon=ft.Icon(ft.Icons.STORE, color=ft.Colors.RED),
                label_content=ft.Text("Store"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.SETTINGS_OUTLINED, color=ft.Colors.ORANGE_300),
                selected_icon=ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.ORANGE_300),
                label_content=ft.Text("Settings"),
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.INFO_OUTLINED, color=ft.Colors.PINK_300),
                selected_icon=ft.Icon(ft.Icons.INFO, color=ft.Colors.PINK_300),
                label_content=ft.Text("About"),
            ),
            # ft.NavigationRailDestination(
            #     icon=ft.Row([ft.Icon(ft.Icons.SETTINGS_OUTLINED), ft.Text("Settings"), ]),
            #     selected_icon_content=ft.Row([ft.Icon(ft.Icons.SETTINGS), ft.Text("Settings"), ]),
            # ),
        ],
        # on_change=lambda e: print("Selected destination:", e.control.selected_index),
        # on_change=lambda e: update_index(e.control.selected_index, data),
        on_change=lambda e: update_body(e.control.selected_index, data),

    )

    # Initialize main content area
    main_content = ft.Column(expand=True)

    # Function to update body content with cards for classes
    def update_body(selected_index, data: fs.Datasy = None):
        if selected_index == 0:  # Classes
            body_content = home_widget(data)
        elif selected_index == 1:  # About
            body_content = ft.Column([
                # Class 1: Python Basics
                ft.Card(
                    content=ft.Column([
                        ft.Text("Page2", size=20, weight=ft.FontWeight.BOLD),
                        ft.Text("Learn the fundamentals of Python programming."),
                    ]),
                ),
            ], )
        elif selected_index == 2:
            body_content = ft.Column([
                # Class 1: Python Basics
                ft.Card(
                    content=ft.Column([
                        ft.Text("store view", size=20, weight=ft.FontWeight.BOLD),
                    ]),
                ),
            ], )
        else:
            body_content = ft.Column([ft.Text("Select a destination!")])

        # Clear and update main content area
        main_content.controls.clear()  # Clear existing controls
        main_content.controls.append(body_content)  # Add new content
        main_content.update()  # Refresh main content
        data.page.update()  # Refresh the page to reflect changes

    def new_controls(index: int):
        print("real control index", index)

        if index == 0:
            # new controls for home
            return [
                ft.Text("Home View"),
            ]
        elif index == 1:
            # new controls for todo
            return [
                ft.Text("Todo View"),
            ]
        elif index == 2:
            # new controls for counter
            return [
                ft.Text("Counter View"),
            ]
        elif index == 3:
            # new controls for store
            return [
                ft.Text("Store View"),
            ]
        else:
            return [ft.Text("Not found")]

    return ft.View(
        "/",

        # controls
        controls=[
            ft.Row([
                rail,
                # ft.VerticalDivider(width=1),

                #
                #
                #
                ft.Card(
                    main_content,
                )
            ], expand=True),
        ],

        # drawer
        drawer=drawer,

        # appbar
        appbar=appbar,
        **kwargs,
    )
