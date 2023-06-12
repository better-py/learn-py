from nicegui import ui, Client


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


@ui.page('/')
def home_page(client: Client):
    client.content.classes(remove='nicegui-content')  # 去除干扰样式！

    div = ui.element('div')
    div.classes("column p-0 m-0 gap-0")
    div.tailwind().padding("0")

    with div:
        h = ui.header(value=True)
        h.tailwind.align_items("center")  # 元素居中
        drawer = ui.left_drawer().classes("bg-gray-900 text-white")  # 提前定义

        with h:
            ui.label('Header').classes("center")
            ui.button(on_click=lambda: drawer.toggle()).props(
                "flat color=white icon=menu round size=sm"
            )

            ui.link('Home', '/').classes("text-red-500 text-solid")

        with drawer:  # top_corner=True, bottom_corner=True
            ui.menu_item('Menu item 1', lambda: ui.open('/page1'))
            ui.menu_item('Menu item 1', lambda: ui.notify("hi!", color="green", position="top"))

        #
        # main content:
        #
        new_tab_view()

        with ui.footer(value=True):
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
    native=True,
    window_size=(1100, 700),
    fullscreen=False,
    reload=True,
    show=True,
)
