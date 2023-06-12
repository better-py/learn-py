from loguru import logger
from nicegui import ui, Client, app


def new_tab_view():
    div = ui.element('q-page')  # 获取指定页面 div 层
    div.classes('row w-full h-full')
    div.tailwind().columns("1").width("screen").height("screen")

    # 底部浮动按钮:
    # with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    #     ui.button(on_click=None).props('fab icon=contact_support')

    with div:
        sp = ui.splitter(value=20)  # 切分分栏比例

        with sp:
            with sp.before:
                d = ui.element("div")
                d.tailwind().columns("1").width("screen").height("screen")

                with d:
                    ui.menu_item('Menu item 1', lambda: ui.open('/page1'))
                    ui.menu_item('Menu item 1', lambda: ui.notify("hi!", color="green", position="top"))

            with sp.after:
                with ui.card().classes("p-10 m-10"):
                    ui.label("new view 1").classes("text-2xl text-red-500")


def new_tab_view2():
    app.title = "new tab view 2"
    d = ui.element('div')
    # d = ui.element('q-page')
    # d = ui.element('nicegui-content')
    d.classes("bg-gray-900 w-full h-full")
    # d.classes("center overflow-hidden")
    # d.classes("bg-gray-900 flex flex-col w-full h-full center overflow-hidden")
    d.classes("p-0 m-0 gap-0")

    with d:
        with ui.card().classes("p-10 m-10"):
            ui.label("page 1 view ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 2 ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 2 ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 2 ")
        with ui.card().classes("p-10 m-10"):
            ui.label("card 2 ")


def page_template(client: Client):
    client.content.classes(remove='nicegui-content')  # 去除干扰样式！
    client.content.classes("flex flex-col w-full h-full")  # fix nicegui-content 样式

    logger.debug(f"page info: {client.page.path}, {client.page.language}")


@ui.page('/')
def home_page(client: Client):
    client.content.classes(remove='nicegui-content')  # 去除干扰样式！
    client.content.classes("flex flex-col w-full h-full")  # fix nicegui-content 样式

    logger.debug(f"main page div: {client.page.path}, {client.page.language}")

    #
    # 更改整个页面的样式:
    #
    client.layout.classes("bg-orange-200")  # 背景色, #21252B
    client.layout.style("background-color: #fef6e4")  # 背景色, #21252B, #f9f4ef, #0f0e17, #232946, #f2f7f5,#fef6e4
    # client.layout.tailwind.border_color("red-500")  # 边框颜色
    # client.layout.tailwind.border_width("2").border_radius("md")  # 边框宽度

    # ui.element('nicegui-content').tailwind.margin("0")  # 背景色

    # client.content.classes("p-0 m-0")

    # client.content.classes(replace="nicegui-content")  # 去除干扰样式！

    div = ui.element('div')  # 如果指定了全局， 会干扰子元素的样式

    # ================================================================================

    h = ui.header(value=True)
    # h.classes('bg-slate-800')
    # h.classes('bg-transparent')
    h.style("background-color: #1F2744")  # #9C7AE6, F99B27, #231641, #0C102E, #1F2744
    h.tailwind.align_items("center")  # 元素居中, [bg-slate-900, purple-600]

    # drawer:
    drawer = ui.left_drawer().classes("bg-slate-900 text-white")  # 提前定义, [bg-gray-900, ]
    drawer.style("background-color: #1F2951")  # [#1F2951, 0C102E]

    with h:
        ui.label('My App').classes("center")
        ui.button(on_click=lambda: drawer.toggle()).props(
            "flat color=white icon=menu round size=sm"
        )

        ui.link('Home', '/').classes("text-red-500 text-solid")

    # ================================================================================

    with drawer:  # top_corner=True, bottom_corner=True
        ui.menu_item('Menu item 1', lambda: ui.open('/page1'))
        ui.menu_item('Menu item 1', lambda: ui.notify("hi!", color="green", position="top"))

    # ================================================================================

    #
    # main content:
    #
    new_tab_view2()

    # ================================================================================

    f = ui.footer(value=True)
    f.classes('bg-slate-800')
    f.style("background-color: #1F2744")  # #9C7AE6, F99B27, #231641, #0C102E, #1F2744

    with f:
        ui.label('Footer')


def new_page1_view():
    with ui.card():
        ui.label("this is page 1 view")


@ui.page('/page1')
def new_page1(client: Client):
    client.content.classes(remove='nicegui-content')  # 去除干扰样式！

    div = ui.element('div')
    div.classes("column p-0 m-0 gap-0")
    div.tailwind().padding("0")

    with div:
        drawer = ui.left_drawer().classes("bg-pink-300")  # 提前定义

        with ui.header(value=True):
            ui.button(on_click=lambda: drawer.toggle()).props(
                "flat color=white icon=menu round size=sm"
            ).classes()
            ui.label('Header')
            ui.link('Home', '/')
            ui.button(on_click=ui.left_drawer.hide).props(
                "flat color=white icon=menu round"
            ).classes("lg:hidden")

        with drawer:  # top_corner=True, bottom_corner=True
            ui.menu_item('Menu item 1', lambda: ui.open('/page1'))
            ui.menu_item('Menu item 1', lambda: ui.notify("hi!", color="green", position="top"))

        #
        # main content:
        #
        new_page1_view()

        with ui.footer(value=True):
            ui.label('Footer')


ui.run(
    title="My App",
    native=True,
    window_size=(1100, 700),
    fullscreen=False,
    reload=True,
    show=True,
)
