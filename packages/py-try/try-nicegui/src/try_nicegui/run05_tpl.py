from util import *


def page_template(client: PageClient):
    client.content.classes(remove='nicegui-content')  # 去除干扰样式！
    client.content.classes("flex flex-col w-full h-full")  # fix nicegui-content 样式

    logger.debug(f"page info: {client.page.path}, {client.page.language}")


@ui.page('/')
def home_page(client: PageClient):
    new_page_template(client)


@ui.page('/page1')
def new_page1(client: PageClient):
    new_page_template(client)


@ui.page('/page2')
def new_page1(client: PageClient):
    def new_view():
        with ui.card().classes('m-5 bg-gray-300'):
            with ui.tabs() as tabs:
                ui.tab('Home', icon='home')
                ui.tab('About', icon='info')

            with ui.tab_panels(tabs, value='Home'):
                with ui.tab_panel('Home'):
                    ui.label('This is the first tab')
                with ui.tab_panel('About'):
                    ui.label('This is the second tab')

    new_page_template(client, new_view)


@ui.page('/page3')
def new_page1(client: PageClient):
    def new_view():
        with ui.card().classes('m-5 bg-gray-300'):
            columns = [
                {'name': 'name', 'label': 'Name', 'field': 'name', 'required': True, 'align': 'left'},
                {'name': 'age', 'label': 'Age', 'field': 'age', 'sortable': True},
            ]
            rows = [
                {'name': 'Alice', 'age': 18},
                {'name': 'Bob', 'age': 21},
                {'name': 'Carol'},
            ]
            ui.table(columns=columns, rows=rows, row_key='name')

    new_page_template(client, new_view)


@ui.page('/page4')
def new_page1(client: PageClient):
    def new_view():
        with ui.card().classes('m-5 bg-gray-300'):
            ui.tree([
                {'id': 'numbers', 'children': [{'id': '1'}, {'id': '2'}]},
                {'id': 'letters', 'children': [{'id': 'A'}, {'id': 'B'}]},
            ], label_key='id', on_select=lambda e: ui.notify(e.value))

    new_page_template(client, new_view)


@ui.page('/page5')
def new_page1(client: PageClient):
    def new_view():
        with ui.card().classes('m-5 bg-gray-300'):
            ui.mermaid('''
            graph LR;
                A --> B;
                A --> C;
            ''')

    new_page_template(client, new_view)


ui.run(
    title="Geek App",
    native=True,
    window_size=(1100, 700),
    fullscreen=False,
    reload=True,
    show=True,
)
