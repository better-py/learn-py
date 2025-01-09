from typing import Sequence

import flet as ft
import flet_easy as fs


def page_layout(
    data: fs.Datasy,
    title: str = None,
    controls: Sequence[ft.Control] | None = None,
    **kwargs,
) -> ft.View:
    drawer = ft.NavigationDrawer(
        selected_index=1,
        controls=[
            ft.Container(
                ft.CircleAvatar(
                    content=ft.Text("Flet", ),
                    width=400,

                ),
                padding=10,
            ),

            ft.Divider(thickness=1),
            # ft.ListView(controls=[], padding=10, ),
            # menu

            ft.Container(

                ft.ListView(
                    [
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.HOME, color=ft.Colors.BLUE, size=30),
                            title=ft.Text("Home"),
                            on_click=data.go("/"),
                            hover_color=ft.Colors.GREY_800,
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.NOTES, color=ft.Colors.ORANGE, size=30),
                            title=ft.Text("Todo"),
                            hover_color=ft.Colors.GREY_800,
                            on_click=data.go("/todo"),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.CALCULATE, color=ft.Colors.GREEN, size=30),
                            title=ft.Text("Counter"),
                            hover_color=ft.Colors.GREY_800,
                            on_click=data.go("/counter"),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.STORE, color=ft.Colors.RED, size=30),
                            title=ft.Text("Store"),
                            hover_color=ft.Colors.GREY_800,
                            on_click=data.go("/store"),
                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.SETTINGS, color=ft.Colors.ORANGE, size=30),
                            title=ft.Text("Settings"),
                            on_click=data.go("/settings"),
                            hover_color=ft.Colors.GREY_800,

                        ),
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.INFO, color=ft.Colors.PINK_300, size=30),
                            title=ft.Text("About"),
                            on_click=data.go("/about"),
                            bgcolor=ft.Colors.TRANSPARENT,
                            hover_color=ft.Colors.GREY_800,
                        ),
                    ],
                    # expand=True,
                    # padding=10,
                    # spacing=5,  # todo x: 间隔

                ),
                # padding=10,
                # bgcolor=ft.Colors.BLUE_ACCENT_400,
            ),

        ],

        # indicator_color=ft.Colors.PINK,
        # shadow_color=ft.Colors.GREEN_ACCENT,
        # bgcolor=ft.Colors.TRANSPARENT,
    )

    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings"),
    ]

    def change_theme(e):
        #
        # todo x: change icon
        #
        e.control.selected = not e.control.selected
        e.control.update()

        # todo x: change theme
        if not data.page:
            return

        # change to light
        if data.page.theme_mode == ft.ThemeMode.DARK or data.page.theme_mode == ft.ThemeMode.SYSTEM:
            data.page.theme_mode = ft.ThemeMode.LIGHT
            data.page.update()
            return

        # change to dark
        data.page.theme_mode = ft.ThemeMode.DARK
        data.page.update()
        return

    appbar = ft.AppBar(
        #
        # open drawer
        #
        leading=ft.IconButton(
            icon=ft.Icons.MENU, on_click=lambda _: data.page.open(drawer)
        ),

        title=ft.Text(title if title else "Home", ),
        center_title=True,
        # toolbar_height=75,
        bgcolor=ft.Colors.ORANGE_ACCENT_400,

        #
        # end open
        #
        actions=[

            #
            # todo x: change theme
            #
            ft.IconButton(
                icon=ft.Icons.LIGHT_MODE,
                selected_icon=ft.Icons.DARK_MODE,
                on_click=lambda e: change_theme(e)),

            ft.Container(
                content=ft.PopupMenuButton(items=appbar_items, bgcolor=ft.Colors.BLUE_ACCENT_400),
                margin=ft.margin.only(left=10, right=10),
            )
        ],
    )

    v = ft.View(
        "/",
        # controls
        controls if controls else [],
        # drawer
        drawer=drawer,
        # appbar
        appbar=appbar,

        # bottom_appbar=ft.BottomAppBar(
        #     bgcolor=ft.Colors.BLUE,
        #     shape=ft.NotchShape.CIRCULAR,
        #     content=ft.Row(
        #         controls=[
        #             ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
        #             ft.Container(expand=True),
        #             ft.IconButton(icon=ft.Icons.SEARCH, icon_color=ft.Colors.WHITE),
        #             ft.IconButton(icon=ft.Icons.FAVORITE, icon_color=ft.Colors.WHITE),
        #         ]
        #     ),
        # ),

        #
        #
        #
        navigation_bar=ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.ORANGE_ACCENT_400,
            inactive_color=ft.Colors.WHITE,
            active_color=ft.Colors.PINK,
            on_change=lambda e: print("Selected tab:", e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
                ft.NavigationBarDestination(icon=ft.Icons.PEOPLE, label="Groups"),
                ft.NavigationBarDestination(icon=ft.Icons.NOTIFICATIONS, label="Notifications"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.BOOKMARK_BORDER,
                    selected_icon=ft.Icons.BOOKMARK,
                    label="Explore",
                ),
            ]
        ),

        padding=10,

        **kwargs,
    )

    # if v.page:
    #     v.page.theme_mode = ft.ThemeMode.LIGHT
    #     v.page.update()

    return v
