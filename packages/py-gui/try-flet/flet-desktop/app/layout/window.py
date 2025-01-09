from typing import Sequence, List

import flet as ft
import flet_easy as fs

from app.widgets.home import home_widget
from loguru import logger


#
# 菜单列表
#
def new_menu() -> List[ft.NavigationRailDestination]:
    return [
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
    ]


def new_drawer(data: fs.Datasy, ) -> ft.NavigationDrawer:
    return ft.NavigationDrawer(
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


def new_appbar(data: fs.Datasy, drawer, title: str = None) -> ft.AppBar:
    appbar_items = [
        ft.PopupMenuItem(text="Login"),
        ft.PopupMenuItem(),  # divider
        ft.PopupMenuItem(text="Settings")
    ]

    logger.debug(f"page locale: {data.page.locale_configuration}")

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

    # 顶部导航栏
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

    return appbar


#
# 窗口布局
#
def window_layout(
    data: fs.Datasy,
    title: str = None,
    controls: Sequence[ft.Control] | None = None,
    **kwargs,
) -> ft.View:
    # todo x: 抽屉
    drawer = new_drawer(data)
    # todo x: 顶部导航栏
    appbar = new_appbar(data, drawer, title)

    #
    # todo x: 主窗口内容容器
    #
    # main_content = ft.Container()  # ft.Column()
    main_content = ft.Column([home_widget(data)], adaptive=True)  # todo x: 默认显示首页, 避免空白

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
            ], expand=True)
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

        # main_content.content = body_content
        main_content.controls.clear()  # Clear existing controls
        main_content.controls.append(body_content)  # Add new content
        main_content.update()  # Refresh main content
        data.page.update()  # Refresh the page to reflect changes

    #
    # todo x: 左侧菜单栏
    #
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.SELECTED,  # 控制显示 label
        # extended=True,
        # min_width=50,
        # min_extended_width=600,
        # leading=ft.FloatingActionButton(
        #     icon=ft.Icons.CREATE, bgcolor=ft.Colors.RED,
        #     on_click=lambda _: data.page.go("/store")),
        # trailing=ft.FloatingActionButton(
        #     icon=ft.Icons.CREATE, bgcolor=ft.Colors.RED,
        #     on_click=lambda _: data.page.go("/counter")),
        # group_alignment=-0.9,

        #
        # 菜单列表
        #

        # TODO X: 菜单列表
        destinations=new_menu(),

        # on_change=lambda e: print("Selected destination:", e.control.selected_index),
        # on_change=lambda e: update_index(e.control.selected_index, data),
        on_change=lambda e: update_body(e.control.selected_index, data),
    )

    #
    # todo x: 布局说明: 顶层容器为一行，左侧为导航栏，右侧为主内容区域
    #
    return ft.View(
        "/",
        controls=[
            ft.Row([
                # todo x: 左侧导航栏
                rail,

                # ft.VerticalDivider(width=1),

                #
                # todo x: 右侧主内容区域
                #
                ft.Card(
                    ft.SafeArea(
                        ft.Container(
                            main_content,
                            padding=10,
                            # margin=10,
                        ),
                    ),
                    expand=True,  # TODO X: 关键参数, 控制卡片的大小铺满窗口
                )
            ],
                expand=True,
            ),
        ],

        # drawer
        drawer=drawer,

        # appbar
        appbar=appbar,
        **kwargs,
    )
