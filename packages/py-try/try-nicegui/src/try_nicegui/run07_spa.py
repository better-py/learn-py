#!/usr/bin/env python3
from nicegui import Client as PageClient
from nicegui import ui

from router import Router
from util import fix_page_layout, new_page_header, new_tab_view2, uh


# from multiprocessing import freeze_support
# freeze_support()  # fix for macos + M1


@ui.page(
    "/"
)  # normal index page (e.g. the entry point of the app)  # all other pages will be handled by the router but must be registered to also show the SPA index page
@ui.page("/{_:path}")
def main(client: PageClient):
    r = Router()

    fix_page_layout(client)
    d = new_drawer(r)
    new_page_header(drawer=d)

    @r.add("/")
    def show_one():
        fix_page_layout(client)

        def new_view():
            with ui.card().classes("m-5 bg-gray-300"):
                columns = [
                    {
                        "name": "name",
                        "label": "Name",
                        "field": "name",
                        "required": True,
                        "align": "left",
                    },
                    {"name": "age", "label": "Age", "field": "age", "sortable": True},
                ]
                rows = [
                    {"name": "Alice", "age": 18},
                    {"name": "Bob", "age": 21},
                    {"name": "Carol"},
                ]
                ui.table(columns=columns, rows=rows, row_key="name")

        new_view()

    @r.add("/two")
    def show_two():
        fix_page_layout(client)
        new_tab_view2()
        # ui.label("Content Two").classes("text-2xl")

    @r.add("/three")
    def show_three():
        fix_page_layout(client)

        def new_view():
            with ui.card().classes("m-5 bg-gray-300"):
                ui.tree(
                    [
                        {"id": "numbers", "children": [{"id": "1"}, {"id": "2"}]},
                        {"id": "letters", "children": [{"id": "A"}, {"id": "B"}]},
                    ],
                    label_key="id",
                    on_select=lambda e: ui.notify(e.value),
                )

        new_view()

    # adding some navigation buttons to switch between the different pages
    # with ui.row():
    #     ui.button("One", on_click=lambda: r.open(show_one)).classes("w-32")
    #     ui.button("Two", on_click=lambda: r.open(show_two)).classes("w-32")
    #     ui.button("Three", on_click=lambda: r.open(show_three)).classes("w-32")

    # this places the content which should be displayed
    r.frame().classes("w-full p-4")  # todo x: 影响全局样式!


def new_drawer(r: Router):
    d = ui.left_drawer()  # todo x: do not pass args !!!
    d.classes("bg-slate-900 text-white")  # 提前定义, [bg-gray-900, ]
    d.style("background-color: #262729")  # [#1F2951, 0C102E, #262729]

    with d:
        uh.list_tile(
            head_icon="home",
            title_text="Home",
            head_color="blue-400",
            on_click=lambda: r.open("/"),
        )
        uh.list_tile(
            head_icon="dashboard_customize",
            title_text="Dashboard",
            head_color="green-400",
            on_click=lambda: r.open("/two"),
        )
        uh.list_tile(
            head_icon="star",
            title_text="Favorite",
            head_color="red-400",
            on_click=lambda: r.open("/three"),
        )

    return d


# ui.run(
#     port=8001,
# )

# ui.run(reload=False, port=native.find_open_port())

ui.run(
    title="Geek App",
    native=False,
    # port=native.find_open_port(),
    reload=False,
    # window_size=(1100, 700),
    fullscreen=False,
    show=True,
)

# if __name__ in {"__main__", "__mp_main__"}:
#     #
#     # https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Multiprocessing
#     #
#     # from multiprocessing import Process, freeze_support
#     #
#     # freeze_support()  # fix for macos + M1
#
#     from os import getpid, getppid
#
#     # import multiprocessing
#     # import sys
#     #
#     # if sys.platform == "darwin":
#     #     ctx = multiprocessing.get_context("spawn")
#     #     Process = ctx.Process
#     #     Queue = ctx.Queue
#     # else:
#     #     Process = multiprocessing.Process
#     #     Queue = multiprocessing.Queue
#
#     logger.info(f"module: {__name__}, pid: {getpid()}, parent pid: {getppid()}")
#
#     ui.run(
#         title="Geek App",
#         native=True,
#         window_size=(1100, 700),
#         fullscreen=False,
#         reload=False,  # todo x: fix for freeze_support()
#         show=True,
#     )
