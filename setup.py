import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Anmol\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Anmol\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="face.ico")]


cx_Freeze.setup(
    name = "Attendance Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'image','data','database','attendance_data']}},
    version = "1.0",
    description = "Face Recognition Automatic Attendace System || Developed By Anmol_Gupta",
    executables = executables
    )
