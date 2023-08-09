import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\StarLord\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\StarLord\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tk8.6"
from cx_Freeze import setup, Executable

base = None

executables = [Executable("gui.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "<Twitter Analyset>",
    options = options,
    version = "<0.1>",
    description = '<Cu Project>',
    executables = executables
)