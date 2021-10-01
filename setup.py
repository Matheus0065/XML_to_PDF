import sys
from cx_Freeze import setup, Executable


base = None
'''if sys.platform == "win32":
    base = "Win32GUI"'''

executables = [
    Executable("base_xml_to_pdf.py", base=base)
]

buildOptions = dict(
    packages=[],
    includes=["selenium", "pyautogui", "zipfile", "datetime"],
    include_files=["chromedriver.exe"],  # "db"
    excludes=[]
)

setup(
    name="XML to PDF",
    description="Automação de lançamentos",
    options=dict(build_exe=buildOptions),
    executables=executables
)
