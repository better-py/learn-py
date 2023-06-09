import os
import subprocess
from pathlib import Path
import nicegui

# app main file
app_file = "src/try_nicegui/run02_tpl.py"

cmd = [
    'python',
    '-m', 'PyInstaller',
    '--clean',
    '--noconfirm',
    '-F',
    '-w',
    app_file,  # your main file with ui.run()
    '--name', 'myapp',  # name of your app
    '--onefile',
    '-i', 'public/images/logo.ico',
    '--windowed',  # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]
subprocess.call(cmd)
