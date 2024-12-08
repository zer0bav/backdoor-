import os
import pyfiglet
from colorama import Fore
import backdoor_listen
import backdoor_create
import other_function
def view():
    while True:
        os.system("clear")
        ascii_art = pyfiglet.figlet_format("c   -   137")
        nothing = pyfiglet.figlet_format("...nothing")



        print(Fore.GREEN + 
            """
                               OOOO
                            OOOOOOOOOO
                         OOO          OOO
                       OOO              OOO
                     OOO   OOOOOOOOOO   OOO
                    OOO   OOO      OOO   OOO
                   OOO   OOO        OOO   OOO
                  OOO   OOO          OOO   OOO
                   OOO   OOO        OOO   OOO
                    OOO   OOO      OOO   OOO
                     OOO   OOOOOOOOOO   OOO
                       OOO              OOO
                         OOO          OOO
                            OOOOOOOOOO
                               OOOO

                                 1
                     CCCCC      11    33333   77777
                    C          1 1        3       7
                    C      --    1    33333      7
                    C            1        3     7
                     CCCCC     11111  33333    7


            """

              )

        print(Fore.RED + "Author: it's ." )




        print(
            Fore.BLUE+

            "[0] Backdoor Create \n"
            "[1] Backdoor Injection \n"
            "[2] Backdoor Listen \n"
            "[3] Exit \n"

        )
        door_choose = (input(Fore.CYAN + "=> " ))



        if door_choose == "0":
            backdoor_create.create_backdoor()
        elif door_choose == "1":
            os.system("clear")
            print(Fore.BLUE + ascii_art)
            other_function.listen_other_server()

        elif door_choose == "2":
            print("nc: 1 or my listenner: 2 ( 1 / 2 ): ")
            x = input(Fore.BLUE +   "=>")
            if x == "1":

                os.system("nc -nvlp 4444")
            elif x == "2":
                backdoor_listen.listen_backdoor()

        elif door_choose == "3":
            exit()
            break

        else:
            
            continue