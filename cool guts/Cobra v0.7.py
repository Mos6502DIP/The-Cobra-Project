import os
from os.path import join
import time
from Mono import system
#Start up
end = True
print("""
░█████╗░░█████╗░██████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██████╦╝██████╔╝███████║
██║░░██╗██║░░██║██╔══██╗██╔══██╗██╔══██║
╚█████╔╝╚█████╔╝██████╦╝██║░░██║██║░░██║
░╚════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝
██╗░░░██╗░█████╗░░░░███████╗
██║░░░██║██╔══██╗░░░╚════██║
╚██╗░██╔╝██║░░██║░░░░░░░██╔╝
░╚████╔╝░██║░░██║░░░░░░██╔╝░
░░╚██╔╝░░╚█████╔╝██╗░░██╔╝░░
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░
The Better call saul Update
By Mos6502  type help for commands v0.8
Boot up sound from the planet x3 ost music made by Anders Enger Jensen
""")
system.play("BOOT.wav")
while end == True:
    try:
        command = input("/>:")

        if command[0:4] == "run."  :

            system.excute(command[4:])

        elif command[0:4] == "bat."  :

            system.batch(command[4:])

        elif command[0:5] == "play.":
            system.play(command[5:])

        elif command[0:3] == "cls":
            os.system('cls')

        elif command[0:3] == "cmd":
            print("Switching to command line interface type (exit) to exit the command line")
            os.system("cmd")

        elif command[0:3] == "dir":
            print("All of your cobra programs")
            os.system("dir /b *.txt")
            

        elif command[0:3] == "os.":
            os.system(command[3:])

        elif command[0:5] == "list.":
            system.read(command[5:])

        elif command == "help":
            system.read(join('Docs', "Help"))

        elif command == "syntax":
            system.read(join('Docs', "syntax"))

        elif command == "changelog":
            system.read(join('Docs', "changelog"))


        elif command == "die" or command == "kys" or command == "exit":
            
             end = False
    except:
        print("Fatal error")
os.system("cls")
print("Bye Bye")
system.play(join('Media' , 'test.mp3'))
        
