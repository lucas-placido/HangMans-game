from cx_Freeze import Executable, setup

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["requests", "time"]}

base = None
setup(
    name="Hangman's game",
    version="2.0",
    description="Hangman's game!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="./icon.ico")],
)
