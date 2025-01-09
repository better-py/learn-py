import flet as ft
import flet_easy as fs
from loguru import logger


def new_chart():
    chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=40,
                        width=40,
                        color=ft.Colors.AMBER,
                        tooltip="Apple",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        color=ft.Colors.BLUE,
                        tooltip="Blueberry",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        color=ft.Colors.RED,
                        tooltip="Cherry",
                        border_radius=0,
                    ),
                ],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=60,
                        width=40,
                        color=ft.Colors.ORANGE,
                        tooltip="Orange",
                        border_radius=0,
                    ),
                ],
            ),
        ],
        border=ft.border.all(1, ft.Colors.GREY_400),
        left_axis=ft.ChartAxis(
            labels_size=40, title=ft.Text("Fruit supply"), title_size=40
        ),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0, label=ft.Container(ft.Text("Apple"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=1, label=ft.Container(ft.Text("Blueberry"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=2, label=ft.Container(ft.Text("Cherry"), padding=10)
                ),
                ft.ChartAxisLabel(
                    value=3, label=ft.Container(ft.Text("Orange"), padding=10)
                ),
            ],
            labels_size=40,
        ),
        horizontal_grid_lines=ft.ChartGridLines(
            color=ft.Colors.GREY_300, width=1, dash_pattern=[3, 3]
        ),
        tooltip_bgcolor=ft.Colors.with_opacity(0.5, ft.Colors.GREY_300),
        max_y=110,
        interactive=True,
        expand=True,
    )
    return chart


def home_widget(data: fs.Datasy):
    logger.debug("data: {}", data.__dict__)

    chart = new_chart()

    return ft.Container(
        ft.SafeArea(
            ft.Card(
                ft.Column([
                    ft.Row([
                        ft.ElevatedButton("Store", on_click=data.go("/store")),
                        ft.ElevatedButton("Home", on_click=data.go("/home")),
                        ft.ElevatedButton("Todo", on_click=lambda _: data.page.go("/todo")),
                        ft.ElevatedButton("Counter", on_click=lambda _: data.page.go("/counter")),
                    ]),

                    ft.Card(
                        content=ft.Column([
                            ft.Text("Class 1: Python Basics", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text("Learn the fundamentals of Python programming."),
                        ], ),
                        expand=True,
                        margin=10,
                    ),

                    ft.Card(chart, ),

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
                ]), )), padding=10)
