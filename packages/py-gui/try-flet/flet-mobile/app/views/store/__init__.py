import flet as ft
import flet_easy as fs

from app.core import app
from app.layout import page_layout


@app.page("/store")
def store_view(data: fs.Datasy):
    tab = ft.Tabs(
        # selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.Icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.Icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
        ],
        expand=1,
        adaptive=True,
        label_color=ft.Colors.ORANGE,
        indicator_color=ft.Colors.ORANGE,
        on_change=lambda index: print(index),
    )

    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("Age"), numeric=True),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("John")),
                    ft.DataCell(ft.Text("Smith")),
                    ft.DataCell(ft.Text("43")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Jack")),
                    ft.DataCell(ft.Text("Brown")),
                    ft.DataCell(ft.Text("19")),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Alice")),
                    ft.DataCell(ft.Text("Wong")),
                    ft.DataCell(ft.Text("25")),
                ],
            ),
        ],
    ),

    return page_layout(
        data,
        title="Store",
        controls=[
            ft.SafeArea(
                ft.Card(
                    ft.Container(
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            [

                                ft.Text("Store page"),

                                ft.Row(table, ),

                                # tab,
                            ]
                        ),
                        padding=10,
                    )
                )
            ),

            #
            # tab view
            #
            tab,

        ],
    )
