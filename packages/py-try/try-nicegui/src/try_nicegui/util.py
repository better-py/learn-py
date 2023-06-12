from typing import Callable

from loguru import logger
from nicegui import Client as PageClient
from nicegui import ui


def fix_page_layout(client: PageClient):
    """修复页面默认布局 & 样式

    """
    client.content.classes(remove='nicegui-content')  # 去除干扰样式！
    client.content.classes("flex flex-col w-full h-full")  # fix nicegui-content 样式

    logger.debug(f"page info: {client.page.path}, {client.page.language}")

    #
    # 更改整个页面的样式:
    #
    client.layout.classes("bg-orange-200")  # 背景色, #21252B
    client.layout.style("background-color: #fef6e4")  # 背景色, #21252B, #f9f4ef, #0f0e17, #232946, #f2f7f5,#fef6e4
    # client.layout.tailwind.border_color("red-500")  # 边框颜色
    # client.layout.tailwind.border_width("2").border_radius("md")  # 边框宽度
    # client.content.classes("p-0 m-0")
    # client.content.classes(replace="nicegui-content")  # 去除干扰样式！


def new_page_drawer(
    fn: Callable = None,
    is_left: bool = True,
) -> ui.left_drawer:
    d = is_left and ui.left_drawer(value=True) or ui.drawer(value=True)
    d.classes("bg-slate-900 text-white")  # 提前定义, [bg-gray-900, ]
    d.style("background-color: #1F2951")  # [#1F2951, 0C102E]

    def new_default():
        ui.menu_item('Menu item 1', lambda: ui.open('/page1'))
        ui.menu_item('Menu item 2', lambda: ui.open('/page2'))
        ui.menu_item('Menu item 3', lambda: ui.open('/page3'))
        ui.menu_item('Menu item 4', lambda: ui.open('/page4'))
        ui.menu_item('Menu item 5', lambda: ui.open('/page5'))
        ui.menu_item('Menu item 6', lambda: ui.notify("hi!", color="green", position="top"))

    with d:
        fn and fn() or new_default()
    logger.debug(f"new_page_drawer: {d}")
    return d


def new_page_header(fn: Callable = None, drawer: ui.left_drawer | ui.drawer = None) -> ui.header:
    h = ui.header(value=True)
    # h.classes('bg-slate-800')
    # h.classes('bg-transparent')
    h.style("background-color: #1F2744")  # #9C7AE6, F99B27, #231641, #0C102E, #1F2744
    h.tailwind.align_items("center")  # 元素居中, [bg-slate-900, purple-600]

    logger.debug(f"headerFn: {fn}, drawer: {drawer}")

    def new_default():
        ui.button(on_click=lambda: drawer.toggle()).props(
            "flat color=white icon=menu round size=sm"
        ).classes()
        ui.label('Header')
        ui.link('Home', '/')

    with h:
        fn and fn() or new_default()
    return h


def new_page_footer():
    f = ui.footer(value=True)
    f.classes('bg-slate-800')
    f.style("background-color: #1F2744")  # #9C7AE6, F99B27, #231641, #0C102E, #1F2744

    with f:
        ui.label('Footer')
    return f


def new_tab_view():
    d = ui.element('div')
    # d = ui.element('q-page')
    # d = ui.element('nicegui-content')
    d.classes("bg-gray-900 w-full h-full")
    # d.classes("center overflow-hidden")
    # d.classes("bg-gray-900 flex flex-col w-full h-full center overflow-hidden")
    d.classes("p-0 m-0 gap-0")

    with d:
        with ui.card().classes("p-10 m-10"):
            ui.label("page 1")


def new_tab_view2():
    d = ui.element('div')
    # d = ui.element('q-page')
    # d = ui.element('nicegui-content')
    d.classes("bg-gray-900 w-full h-full")
    # d.classes("center overflow-hidden")
    # d.classes("bg-gray-900 flex flex-col w-full h-full center overflow-hidden")
    d.classes("p-0 m-0 gap-0")

    with d:
        with ui.card().classes("p-10 m-10"):
            ui.label("card 1")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 2 ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 3 ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 4 ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 5 ")


def new_page_template(client: PageClient, content: Callable = None):
    fix_page_layout(client)

    # drawer:
    d = new_page_drawer()

    new_page_header(drawer=d)

    #
    # content:
    #
    content() if content else new_tab_view2()

    new_page_footer()
