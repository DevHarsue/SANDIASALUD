from cx_Freeze import setup, Executable

setup(
    name="SANDIASALUD",
    version="1.0",
    description="Aplicacion para ginecologia",
    executables=[Executable("main.py", base="Win32GUI", icon="images/logo.ico")]
)