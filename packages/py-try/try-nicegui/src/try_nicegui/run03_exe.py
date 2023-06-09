import sys
from nicegui import ui

ui.label('Hello from PyInstaller')

# sys.stdout = open('logs.log', 'w')


ui.run(
    native=True,
    window_size=(500, 400),
    fullscreen=False,
    reload=False,
    show=False
)
