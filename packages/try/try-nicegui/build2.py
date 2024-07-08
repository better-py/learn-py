import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "path": sys.path + ["src/try_nicegui"],  # add your own path
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

directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("MyProgramMenu", "ProgramMenuFolder", "MYPROG~1|My Program"),
]

msi_data = {
    "Directory": directory_table,
    "ProgId": [
        ("Prog.Id", None, None, "This is a description", "IconId", None),
    ],
    "Icon": [
        ("IconId", "icon.ico"),
    ],
}

bdist_msi_options = {
    "add_to_path": True,
    "data": msi_data,
    "environment_variables": [
        ("E_MYAPP_VAR", "=-*MYAPP_VAR", "1", "TARGETDIR")
    ],
    "upgrade_code": "{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}",
}

# macos options
bdist_mac_options = {
    "bundle_name": "MyApp",
    # "custom_info_plist": "Info.plist",
    # "iconfile": "icon.icns",
}

bdist_dmg_options = {
    "volume_label": "MYAPP",
    "applications_shortcut": True,
    # "background": "background.png",
    # "custom_icon": "icon.icns",
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
        # "bdist_msi": bdist_msi_options,
        "bdist_mac": bdist_mac_options,
        "bdist_dmg": bdist_dmg_options,
    },
    executables=[Executable(
        exe_file,
        base=base,
        icon='public/images/logo.ico'
    )],
)
