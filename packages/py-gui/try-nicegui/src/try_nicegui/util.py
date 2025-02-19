from typing import Callable

from loguru import logger
from nicegui import Client as PageClient
from nicegui import ui


class UIHelper(object):
    """UI 组件
    """

    def empty(self, size: str = 'xs'):
        """空行
        """
        e = ui.row()
        with e:
            ui.icon('home', size=size, color='transparent')
        return ui.row()

    def list_tile(
        self,
        head: Callable = None,
        head_icon: str = 'rocket',
        head_color: str = 'primary',
        head_size: str = 'sm',

        #
        title: Callable = None,
        title_text: str = None,

        #
        tail: Callable = None,
        tail_icon: str = None,
        tail_color: str = 'primary',
        tail_size: str = 'sm',

        on_click: Callable = None,

        #
        #
        #
        bold: bool = False,
        has_border: bool = False,
        has_tooltip: bool = False,
    ) -> ui.row:
        """传 lambda 构造函数， 不能直接传一个组件， 会多画一个组件（创建，即绘制）
        :icon: 一个函数，返回一个组件, 可以使用 lambda
        :title: 一个函数，返回一个组件, 可以使用 lambda
        """

        el = ui.row()
        # 样式：hover:bg-gray-200
        el.tailwind("hover:bg-gray-600 cursor-pointer").padding("p-2").margin("my-3").border_radius("md")  # 间距
        el.tailwind.align_items("center")  # 元素居中, [bg-slate-900, purple-600]

        # 点击事件：
        el.on(
            'click',
            lambda: on_click() if on_click else ui.notify(
                "click menu item", color="orange", closeBtn=True, position="top",
            ),
        )

        has_tooltip and el.tooltip(title_text or "click menu item")
        has_border and el.tailwind().border_style("solid").border_width("2")

        def default_title(text: str = None):
            w = ui.label(text or 'Menu Item')
            w.classes("text-1xl text-white")
            return w

        # 组件元素：
        with el:
            # 头
            head() if head else ui.icon(head_icon, size=head_size, color=head_color)
            # 标题
            title() if title else default_title(title_text)
            # 尾
            tail() if tail else (ui.icon(tail_icon, size=tail_size, color=tail_color) if tail_icon else None)
        return el

    def menu_list(self):
        """菜单列表
        """

        ui.label("Menu")

        uh.empty()
        ui.separator().tailwind("bg-gray-600").height("0.5")  # 背景色

        self.list_tile(head_icon="home",
                       title_text="Home",
                       head_color="blue-400",
                       on_click=lambda: ui.open("/"))
        self.list_tile(head_icon="dashboard_customize",
                       title_text="Dashboard",
                       head_color="green-400",
                       on_click=lambda: ui.open("/page1"))
        self.list_tile(head_icon="pending",
                       title_text="Inbox",
                       head_color="orange-300",
                       on_click=lambda: ui.open("/page2"))
        self.list_tile(head_icon="edit",
                       title_text="Edit",
                       head_color="red-400",
                       on_click=lambda: ui.open("/page3"))
        self.list_tile(head_icon="star",
                       title_text="Favorite",
                       head_color="yellow-400",
                       on_click=lambda: ui.open("/page4"))
        self.list_tile(head_icon="thumb_up",
                       title_text="Star",
                       head_color="green-200",
                       on_click=lambda: ui.open("/page5"))

        ui.separator().tailwind("bg-gray-600").height("0.5")  # 背景色

        self.list_tile(head_icon="workspace_premium",
                       title_text="Premium",
                       head_color="purple-300",
                       on_click=lambda: ui.notify("hi!", color="green", position="top"))
        self.list_tile(head_icon="settings", title_text="Settings", head_color="blue-300")
        self.list_tile(head_icon="lightbulb", title_text="About", head_color="red-300")


uh = UIHelper()


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
    client.layout.style("background-color: #202123")  # 背景色, #21252B, #f9f4ef, #0f0e17, #232946, #f2f7f5,#fef6e4
    # client.layout.tailwind.border_color("red-500")  # 边框颜色
    # client.layout.tailwind.border_width("2").border_radius("md")  # 边框宽度
    # client.content.classes("p-0 m-0")
    # client.content.classes(replace="nicegui-content")  # 去除干扰样式！


def new_menu():
    UIHelper.list_tile()

    pass


def new_page_drawer(
    fn: Callable = None,
    is_left: bool = True,
) -> ui.left_drawer:
    d = is_left and ui.left_drawer(value=True) or ui.drawer(value=True)
    d.classes("bg-slate-900 text-white")  # 提前定义, [bg-gray-900, ]
    d.style("background-color: #262729")  # [#1F2951, 0C102E, #262729]

    def new_default():
        ui.menu_item('Menu item 1', lambda: ui.open('/page1'))
        ui.menu_item('Menu item 2', lambda: ui.open('/two'))
        ui.menu_item('Menu item 3', lambda: ui.open('/page3'))
        ui.menu_item('Menu item 4', lambda: ui.open('/page4'))
        ui.menu_item('Menu item 5', lambda: ui.open('/page5'))
        ui.menu_item('Menu item 6', lambda: ui.notify("hi!", color="green", position="top"))

    def new_menu2():
        uh.menu_list()

    with d:
        fn and fn() or new_menu2()
    logger.debug(f"new_page_drawer: {d}")
    return d


def new_page_header(fn: Callable = None, drawer: ui.left_drawer | ui.drawer = None) -> ui.header:
    e = ui.header(value=True)
    # h.classes('bg-slate-800')
    # h.classes('bg-transparent')
    e.style("background-color: #1F2744")  # #9C7AE6, F99B27, #231641, #0C102E, #1F2744
    e.style("background-color: #262729")  # #9C7AE6, F99B27, #231641, #0C102E, #1F2744
    e.tailwind.align_items("center")  # 元素居中, [bg-slate-900, purple-600]

    logger.debug(f"headerFn: {fn}, drawer: {drawer}")

    def new_default():
        with ui.row().classes("items-center").on('click', lambda: ui.open("/")):
            ui.icon('flutter_dash', color='yellow-400', size='md')
            ui.label('Geek App').classes('text-h6 text-yellow-400')

        uh.empty()
        uh.empty()
        with ui.row().classes("items-center").on('click', lambda: drawer.toggle()):
            ui.icon('menu', color='green-400', size='sm')

    with e:
        fn and fn() or new_default()
    return e


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
    d.classes("w-full h-full")
    # d.classes("center overflow-hidden")
    # d.classes("bg-gray-900 flex flex-col w-full h-full center overflow-hidden")
    d.classes("p-0 m-0 gap-0")

    with d:
        with ui.card().classes("p-5 m-5 bg-gray-300"):
            ui.label("card 1")
        with ui.card().classes("p-5 m-5 bg-gray-300"):
            ui.label("card 2 ")
        with ui.card().classes("p-5 m-5 bg-gray-300"):
            ui.label("card 3 ")
        with ui.card().classes("p-5 m-5 bg-gray-300"):
            ui.label("card 4 ")
        with ui.card().classes("p-5 m-5 bg-gray-300"):
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

    # new_page_footer()
