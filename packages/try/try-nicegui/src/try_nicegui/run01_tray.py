from multiprocessing import freeze_support

from nicegui import app, ui
from PIL import Image
from pystray import Icon, Menu, MenuItem
from loguru import logger
import sys
import multiprocessing

if sys.platform == 'darwin':
    ctx = multiprocessing.get_context('spawn')
    Process = ctx.Process
    Queue = ctx.Queue

else:
    Process = multiprocessing.Process
    Queue = multiprocessing.Queue

#################################################################

logo_file = "public/images/logo.png"

app_process = None
g_tray = None

app.native.window_args['resizable'] = False
app.native.start_args['debug'] = False

ui.label('app running in native mode')
ui.button('enlarge', on_click=lambda: app.native.main_window.resize(800, 600))


#################################################################

def new_tray():
    global g_tray

    def on_exit(icon, item):
        logger.warning("tray: exit start...")
        app.shutdown()
        logger.warning("tray: exit end...")

    def show_app():
        app.native.main_window.show()

    image = Image.open(logo_file)
    menu = Menu(
        # MenuItem('Open', on_open),
        MenuItem("Show App", show_app),
        MenuItem("Notify Hello", lambda: logger.info("tray: hello!")),
        MenuItem('Exit', on_exit),
    )

    g_tray = Icon('Pystray', icon=image, menu=menu)
    return g_tray


def run_app():
    ui.run(native=True, window_size=(500, 400), fullscreen=False, reload=False, show=False)


def start_app_process():
    global app_process

    app_process = Process(target=run_app)
    app_process.start()
    logger.warning("start_app_process")
    return app_process


#################################################################

# ui.run(native=True, window_size=(500, 400), fullscreen=False)

freeze_support()  # not work

# start_app_process() # not work

tray = new_tray()
# tray.run()
tray.run_detached(setup=run_app())  # use this
tray.stop()
logger.warning("app exit...")
