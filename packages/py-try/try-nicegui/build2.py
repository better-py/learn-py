import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "includes": [
        "nicegui",
        "loguru",
        # "pillow",
        # "pywebview",
        # "typer"
    ],
    "packages": ["os", "sys", "json", "time", "threading", "subprocess", "shutil", "pathlib", "typing"],
    "zip_include_packages": ["encodings", "PySide6"],
}

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

# GUI app
exe_file = 'src/try_nicegui/run05_tpl.py'

#
# ref: https://cx-freeze.readthedocs.io/en/latest/setup_script.html
#
setup(
    name="myapp",
    version="0.1",
    description="My GUI application!",
    options={
        "build_exe": build_exe_options,
    },
    executables=[Executable(exe_file, base=base)],
)
