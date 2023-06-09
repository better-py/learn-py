import sys
from nicegui import ui
from nicegui import app, ui
ui.label('Hello from PyInstaller')

# sys.stdout = open('logs.log', 'w')
app.native.window_args['resizable'] = False
app.native.start_args['debug'] = False


ui.run(
    native=True,
    window_size=(500, 400),
)
