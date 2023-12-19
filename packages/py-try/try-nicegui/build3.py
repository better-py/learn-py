import os
import subprocess
from pathlib import Path
import nicegui


app_file = "src/try_nicegui/run02_tpl.py"
app_file = "src/try_nicegui/run07_spa.py"  # packages/py-try/try-nicegui/src/try_nicegui/run03_exe.py


cmd = [
    "python",
    "-m",
    "PyInstaller",
    app_file,  # your main file with ui.run()
    "--name",
    "myapp",  # name of your app
    "--onefile",
    # "-D",
    # "--clean",
    # "--onedir", # todo x: mem leak!
    "--noconfirm",
    # "--noconsole",
    "--path",
    "src/try_nicegui",
    # "--windowed",  # prevent console appearing, only use with ui.run(native=True, ...)
    "--add-data",
    f"{Path(nicegui.__file__).parent}{os.pathsep}nicegui",
]
subprocess.call(cmd)
