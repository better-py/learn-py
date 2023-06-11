from nicegui import ui, Client


def new_tab_view():
    div = ui.element('q-page')  # 获取指定页面 div 层
    div.classes('row')

    with div:
        sp = ui.splitter(value=20)  # 切分分栏比例

        with sp:
            with sp.before:
                tabs = ui.tabs().props("vertical inline-label")
                tabs.classes("bg-gray-900 text-yellow  shadow-2")  # 横向控制
                tabs.tailwind().align_items("start")
                with tabs:
                    ui.tab('Home', icon='home')
                    ui.tab('Profile', icon='rocket')
                    ui.tab('About', icon='info')

            with sp.after:
                panels = ui.tab_panels(tabs, value='Home').props("vertical animated swipeable")
                panels.classes("bg-gray-200 shadow-2 w-3/4 h-full")
                panels.tailwind().columns("1").width("screen")

                with panels:
                    with ui.tab_panel('Home'):
                        with ui.card().classes("w-full h-full m-2"):
                            ui.label("new view 1").classes("text-2xl text-red-500")
                    with ui.tab_panel('Profile'):
                        with ui.card().classes("w-full h-full m-2"):
                            ui.label("new view 2").classes("text-2xl text-green-500")
                    with ui.tab_panel('About'):
                        with ui.card().classes("w-full h-full m-2"):
                            ui.label("new view 3").classes("text-2xl text-blue-500")


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
