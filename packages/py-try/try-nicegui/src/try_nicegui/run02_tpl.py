import click
from nicegui import app, ui


@ui.page('/')
def home():
    ui.label('app running in native mode')
    ui.button('enlarge', on_click=lambda: app.native.main_window.resize(800, 600))


@click.command()
@click.option('--mode', default="web")
def main(mode: str = True):
    """命令行传参， 启动

    :param mode: 运行方式，web 或 native
    :return:
    """
    if mode.lower() == "web":
        ui.run()
    elif mode.lower() == "native" or mode.lower() == "desktop":
        app.native.window_args['resizable'] = False
        app.native.start_args['debug'] = False
        ui.run(
            native=True,
            window_size=(500, 400),
            fullscreen=False,
            reload=False,
            show=False
        )


if __name__ == '__main__':
    main()
