from nicegui import ui, Client


def new_tab_view():
    div = ui.element('q-page')  # 获取指定页面 div 层
    div.classes('row w-full h-full')
    div.tailwind().columns("1").width("screen").height("screen")

    with div:
        sp = ui.splitter(value=20)  # 切分分栏比例

        with sp:
            with sp.before:
                d = ui.element("div")
                d.tailwind().columns("1").width("screen").height("screen")

                with d:
                    ui.menu_item('Menu item 1', lambda: ui.notify("hi!", color="orange", position="top"))
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
        with ui.header(value=True):
            ui.label('Header')

        #
        # main content:
        #
        new_tab_view()

        with ui.footer(value=True):
            ui.label('Footer')


@ui.page('/page1')
def new_page1():
    with ui.card():
        ui.label('page1')


ui.run(
    window_size=(1100, 700),
    fullscreen=False,
    reload=True,
    show=True,
)
