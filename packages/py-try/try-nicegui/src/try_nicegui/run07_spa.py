#!/usr/bin/env python3
from nicegui import ui
from nicegui import Client as PageClient
from router import Router
from util import fix_page_layout, new_page_header, new_tab_view2, uh


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

        ui.card().classes("p-5 m-5 bg-gray-300")
        ui.card().classes("p-5 m-5 bg-gray-300")

        ui.label("Content One").classes("text-2xl")

    @r.add("/two")
    def show_two():
        fix_page_layout(client)
        new_tab_view2()
        # ui.label("Content Two").classes("text-2xl")

    @r.add("/three")
    def show_three():
        fix_page_layout(client)

        ui.card().classes("p-5 m-5 bg-gray-300")
        ui.card().classes("p-5 m-5 bg-gray-300")

        ui.label("Content Three").classes("text-2xl")

    # adding some navigation buttons to switch between the different pages
    # with ui.row():
    #     ui.button("One", on_click=lambda: r.open(show_one)).classes("w-32")
    #     ui.button("Two", on_click=lambda: r.open(show_two)).classes("w-32")
    #     ui.button("Three", on_click=lambda: r.open(show_three)).classes("w-32")

    # this places the content which should be displayed
    r.frame().classes("w-full p-4 bg-gray-100")


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


ui.run(
    title="Geek App",
    native=True,
    window_size=(1100, 700),
    fullscreen=False,
    reload=True,
    show=True,
)
