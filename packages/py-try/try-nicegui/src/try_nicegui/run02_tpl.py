from typing import Optional, Callable

import click
from loguru import logger
from nicegui import app, ui, Client


def list_tile(
    icon_symbol: str = None,
    title_text: str = None,
    icon: Callable = None,
    title: Callable = None,
    on_click: Callable = None,
    has_border: bool = False,
    has_tooltip: bool = False,
) -> ui.row:
    """传 lambda 构造函数， 不能直接传一个组件， 会多画一个组件（创建，即绘制）
    :icon: 一个函数，返回一个组件, 可以使用 lambda
    :title: 一个函数，返回一个组件, 可以使用 lambda
    """

    # 点击事件：
    tile = ui.row().on(
        'click',
        lambda: on_click() if on_click else ui.notify(
            "click menu item", color="orange", closeBtn=True, position="top",
        ),
    )

    has_tooltip and tile.tooltip(title_text or "click menu item")
    has_border and tile.tailwind().border_style("solid").border_width("2")

    # 样式：hover:bg-gray-200
    tile.tailwind("hover:bg-gray-300 cursor-pointer").padding("p-2").margin("my-3").border_radius("md")  # 间距

    # 组件元素：
    with tile:
        icon and icon() or ui.icon(icon_symbol or 'rocket', size='md', color='primary')
        title() if title else ui.label(title_text or 'Menu Item').tailwind("text-2xl").text_color("primary")
    return tile


def side_menu() -> ui.left_drawer:
    """侧边栏菜单：

    样式说明：
      - no-wrap : 不换行
      - gap-1 : menu item 间距 1
      - mt-[-32px] : margin-top -32px
      - px-5 : 左右 padding 5px
      - py-10 : 上下 padding 10px
      - width: calc(80%) : 宽度 80%

    """
    result = ui.label().classes('mr-auto text-2xl yellow-11')

    bg_color = "#272343"  # 背景色

    # 抽屉+样式：
    drawer = ui.left_drawer(value=True)
    drawer.classes("gap-2 mt-[-32px] overflow-y-scroll")  # fixme: hacked! mt-[-32px]
    drawer.style("height: calc(100% + 32px) !important;")  # fixme: hacked! calc(100% + 32px)
    # drawer.style("width: calc(80%) !important;")  # fixme: hacked! calc(80%)
    # drawer.style(f"background-color: {bg_color};")  # 背景色
    drawer.tailwind("overflow-y-scroll bg-gray-900").columns("1").padding("5").margin(
        "5").gap("5").overscroll_behavior("y-auto")

    # 抽屉元素：
    with drawer:
        ui.avatar('favorite_border', text_color='grey-11', ).tailwind().margin("my-5")

        ui.separator().tailwind("bg-green-100")  # 背景色

        list_tile(icon=lambda: ui.avatar('home', size='md', color='orange-300', square=True))
        list_tile(icon=lambda: ui.avatar('edit', size='md', color='green-400'))
        list_tile(icon=lambda: ui.avatar('thumb_up', size='md', color='yellow-500'))
        list_tile()
        list_tile(icon_symbol="star", title_text="Menu Star", has_border=True)
        list_tile(icon=lambda: ui.icon('home', size='md', color='red-600').tailwind("text-2xl"))
        list_tile(icon=lambda: ui.icon('thumb_up', size='md', color='green-600').tailwind("text-2xl"))

        ui.separator().tailwind("bg-green-100")  # 背景色

        ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1')).classes('text-2xl')
        ui.separator().tailwind("bg-green-100")  # 背景色

    return drawer


def add_header(menu: Optional[ui.left_drawer] = None) -> None:
    menu_items = {
        "content": "/#content",
        "Features": "/#features",
        "Demos": "/#demos",
        "Documentation": "/documentation",
        "Examples": "/#examples",
        "Why?": "/#why",
    }
    with ui.header().classes("items-center duration-200 p-0 px-4 no-wrap").style(
        "box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1)"
    ):
        if menu:
            ui.button(on_click=menu.toggle).props(
                "flat color=white icon=menu round"
            ).classes("lg:hidden")
        with ui.link(target=home).classes("row gap-4 items-center no-wrap mr-auto"):
            ui.icon("home")
            # svg.face().classes("w-8 stroke-white stroke-2")
            # svg.word().classes("w-24")
        with ui.row().classes("max-lg:hidden"):
            for title, target in menu_items.items():
                ui.link(title, target).classes(replace="text-lg text-white")

        # ============================================================================

        #
        #
        #
        with ui.link(target="https://discord.gg/TEpFeAaF4f").classes(
            "max-[435px]:hidden"
        ).tooltip("Discord"):
            ui.label("Discord").classes("text-white")
            # svg.discord().classes("fill-white scale-125 m-1")
        with ui.link(target="https://www.reddit.com/r/nicegui/").classes(
            "max-[385px]:hidden"
        ).tooltip("Reddit"):
            # svg.reddit().classes("fill-white scale-125 m-1")
            ui.label("Reddit").classes("text-white")
        with ui.link(target="https://github.com/zauberzeug/nicegui/").tooltip("GitHub"):
            # svg.github().classes("fill-white scale-125 m-1")
            ui.label("GitHub").classes("text-white")
        # add_star().classes("max-[480px]:hidden")
        with ui.row().classes("lg:hidden"):
            with ui.button().props("flat color=white icon=more_vert round"):
                with ui.menu().classes("bg-primary text-white text-lg").props(
                    remove="no-parent-event"
                ):
                    for title, target in menu_items.items():
                        ui.menu_item(
                            title, on_click=lambda _, target=target: ui.open(target)
                        )


def new_footer():
    footer_color = "#ff8e3c"  # #140d0b # #ff8e3c
    ft = ui.footer(value=True)  # .style(f"background-color: {footer_color}")
    ft.tailwind("bg-gray-800")
    with ft:
        ui.label("Footer")


def new_main_content():
    """页面主体部分

    """
    pass


def new_menu_page():
    """点击页面， 切换不同的页面内容

    """
    pass


@ui.page("/")
def home(client: Client):
    logger.debug("home page")

    ui.add_head_html('<style>html {scroll-behavior: auto;}</style>')

    # 左侧菜单栏：
    menu = side_menu()

    # 顶部 header：
    add_header(menu)

    tabs = ui.tabs().props("vertical")
    tabs.tailwind().columns("1")

    with tabs:
        ui.tab('Home', icon='home')
        ui.tab('About', icon='info')

    panels = ui.tab_panels(tabs, value='Home').props("full-width vertical")
    panels.classes("p-8 bg-gray-100 rounded-lg shadow-lg")
    panels.tailwind().columns("1").vertical_align("middle")

    with panels:
        with ui.tab_panel('Home'):
            ui.label('This is the first tab')
        with ui.tab_panel('About'):
            ui.label('This is the second tab')

    #
    #
    #
    ui.label("app running in native mode")
    ui.button("enlarge", on_click=lambda: app.native.main_window.resize(1100, 700))

    # main content:
    with ui.column().classes('w-full p-8 lg:p-16 max-w-[1250px] mx-auto'):
        # section_heading('Reference, Demos and more', '*NiceGUI* Documentation')
        ui.markdown('''
            This is the documentation for NiceGUI >= 1.0.
            Documentation for older versions can be found at [https://0.9.nicegui.io/](https://0.9.nicegui.io/reference).
        ''').classes('bold-links arrow-links')

    ui.link('show page with fancy layout', page_layout)
    ui.link(text="content", target="/content", )

    #
    # 底部
    #
    new_footer()


@ui.page("/content")
def home_content(name: str, client: Client):
    logger.debug("click route content")
    ui.label("home content")


@ui.page('/page_layout')
def page_layout():
    logger.debug("page layout")
    ui.label('CONTENT')
    [ui.label(f'Line {i}') for i in range(100)]
    with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        ui.label('HEADER')
        ui.button(on_click=lambda: right_drawer.toggle()).props('flat color=white icon=menu')
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.label('LEFT DRAWER')
    with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
        ui.label('RIGHT DRAWER')
    with ui.footer().style('background-color: #3874c8'):
        ui.label('FOOTER')


@click.command()
@click.option("--mode", default="native")
def main(mode: str = True):
    """命令行传参， 启动

    :param mode: 运行方式，web 或 native
    :return:
    """
    if mode.lower() == "web":
        ui.run()
    elif mode.lower() == "native" or mode.lower() == "desktop":
        app.native.window_args["resizable"] = False
        app.native.start_args["debug"] = False

        logger.debug("app running in native mode")
        ui.run(
            native=True,
            window_size=(1100, 700),
            fullscreen=False,
            reload=False,
            show=True,
        )

    logger.debug("app exit...")


ui.run(
    native=True,
    window_size=(1100, 700),
    fullscreen=False,
    reload=True,
    show=True,
)

# if __name__ == '__main__':
#     main()
