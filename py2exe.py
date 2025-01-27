import os
import subprocess

def py_exe():
    exe_input = input("please enter the exe file name (without .exe): ")
    icon = input("please enter the icon file name: ")
    python_file = "project.py"

    if not os.path.exists(python_file):
        print("file not found")
        return
    if not os.path.exists(icon):
        print(f"Error: Icon file '{icon}' not found!")
        return
    try:
        print("Converting Python script to EXE...")
        subprocess.run([
            "pyinstaller",
            "--onefile",
            "--noconsole",
            f"--icon={icon}",
            f"--name={exe_input}",
            python_file
        ], check=True)
        print(f"Conversion successful! EXE created as 'dist/{exe_input}.exe'")
    except subprocess.CalledProcessError as e:
        print(f"Error during PyInstaller execution: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")



