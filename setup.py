import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages" : ["random_word"],
    "includes": ["draw", "word"]    
}

base = None
setup(
    name="Hangman's game",
    version="1.0",
    description="Hangman's game!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)