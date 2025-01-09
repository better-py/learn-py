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
    logger.debug(f"home view: {data.page}")

    chart = new_chart()

    l = ft.ListView(
        [
            ft.ListTile(
                leading=ft.Icon(ft.Icons.BUILD, color=ft.Colors.RED),
                title=ft.Text("list2"),
                subtitle=ft.Text("sub"),
                trailing=ft.Icon(ft.Icons.CHECK, color=ft.Colors.GREEN),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.BOOK, color=ft.Colors.GREEN),
                title=ft.Text("list2"),
                subtitle=ft.Text("sub"),
                expand=True,
                trailing=ft.Icon(ft.Icons.CHECK, color=ft.Colors.GREEN),
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.BADGE, color=ft.Colors.BLUE),
                title=ft.Text("list2"),
                subtitle=ft.Text("sub"),
                trailing=ft.Icon(ft.Icons.CHECK, color=ft.Colors.GREEN),
            ),
        ],
        padding=10,
        expand=True,
        adaptive=True,
    )

    return ft.Container(
        ft.Column([
            ft.Card(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Class 1: Python Basics", size=20, weight=ft.FontWeight.BOLD),
                            ft.Text("Learn the fundamentals of Python programming."),

                            l,
                        ],
                        adaptive=True,
                    ),
                    padding=10,
                    expand_loose=True,
                    expand=True,
                ),
                expand=True,

            )
        ]),
    )

    return ft.Container(
        ft.Column([
            ft.Text("Class 1: Python Basics", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Learn the fundamentals of Python programming."),

            ft.Container(
                bgcolor=ft.colors.GREEN_200,
                expand=True,
            ),

            ft.Text("Learn the fundamentals of Python programming."),

            # ft.ListView(
            #     [
            #         ft.ListTile(trailing=ft.Icon(ft.Icons.BUILD),
            #                     title=ft.Text("list2")),
            #         ft.ListTile(trailing=ft.Icon(ft.Icons.BOOK),
            #                     title=ft.Text("list2")),
            #         ft.ListTile(trailing=ft.Icon(ft.Icons.BADGE),
            #                     title=ft.Text("list2")),
            #
            #     ]
            # )

        ]),

        # alignment=ft.alignment.center,
        # expand=True,
    )

    return ft.Card(
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
        ]), margin=10, expand=True, )

    # return ft.Container(
    #     ft.SafeArea(
    #         , padding=10)
