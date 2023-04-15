from playsound import playsound
from os.path import join
import os
import time
import msvcrt

def excute(file_name):
    #var set
    printflt = False
    cache = {}
    count = 0
    
    cache_ins = ""
    cache_str = ""
    int_cache = {}
    cache_bol = True
    #file read


    # file to chache
    with open(file_name+".txt", "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            count += 1
            cache[count] = line.strip()

    #reset count
    count = 0
    # excute
    while count <= int(len(cache)-1):
            #Recall instruction
            count += 1
            
            item = cache[count]
            #set instruction
            
            # print str
            if item[0:5] == "print":
                
                if substring(item)[0:4] == "var.":
                    if printflt == True:
                        
                        if isdata(item) == "True":
                            
                            print(int_cache[subvar(item , 2)] , subvar(item , 3))
                        else:
                            print(int_cache[subvar(item , 2)])
                    else:
                        
                        if isdata(item) == "True":
                            print(int(int_cache[subvar(item , 2)]) , subvar(item , 3))
                        else:
                            print(int(int_cache[subvar(item , 2)]))


                           
                else:
                    print(substring(item))
            

            # print var


            
                    
                
            # goto line
            elif item[0:4] == "goto":
                if substring(item)[0:4] == "var.":
                    count = int(int_cache[subvar(item , 2)] - 1)
                else:
                    count = int(substring(item))-1
                    
            # + var 
            elif item[0:5] == "var+.":
                int_cache[subvar(item , 1)] = float(int_cache[subvar(item , 1)]) + float(substring(item))
            #  set a varible
            elif item[0:5] == "var=.":
                int_cache[subvar(item , 1)] = float(substring(item))

           #print chache of in
            elif item == "varcache()":
                print(int_cache)

            # play sound
            elif item[0:9] == "playsound":
                play(substring(item))

            #os command
            elif item[0:2] == 'os':
                os.system(substring(item))

            #pause
            elif item[0:5] == "pause":
                if substring(item)[0:4] == "var.":
                    time.sleep(float(int_cache[subvar(item , 2)]))
                else:
                    time.sleep(float(substring(item)))

            # let's you print a float
            elif item[0:8] == "fltprint":
                printflt = bool(substring(item))

            

            else:
                print("Error on line:",count)

            if msvcrt.kbhit() and msvcrt.getch().decode() == chr(27):
                print(f"CODE BREAK AT LINE {count}!")

                break

        

    

def read(file_name):
    try:
        with open(file_name+".txt", "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                print(line.strip())
    except:
        print("fatal error")
def substring(string):
    start = string.index('(')
    end = string.index(')',start+1)
    return(string[start+1:end])

def subvar(var , mode):
    if mode == 1:
        start = var.index('.')
        end = var.index('(',start+1)
        return(var[start+1:end])
    elif mode == 2:
        start = var.index('.')
        end = var.index(')',start+1)
        return(var[start+1:end])
    elif mode == 3:
        start = var.index('[')
        end = var.index(']',start+1)
        return(var[start+1:end])
    elif mode == 4:
        start = var.index(')')
        end = var.index('[',start+1)
        return(var[start+1:end])

def play(file):
    playsound.playsound(join("Media" , file))


def isdata(item):
    
    if item[len(item)-1] == "]":
        return("True")
    else:
        return("False")

def batch(file_name):
    #var set
    printflt = False
    cache = {}
    count = 0
    
    #file read


    # file to chache
    with open(file_name+".cbrbat", "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            count += 1
            cache[count] = line.strip()

    #reset count
    count = 0
    # excute
    while count <= int(len(cache)-1):
            #Recall instruction
            count += 1
            
            command = cache[count]

            if command[0:4] == "run."  :

                excute(command[4:])

            elif command[0:5] == "play.":
                play(command[5:])

            elif command[0:3] == "cls":
                os.system('cls')

            elif command[0:3] == "os.":
                os.system(command[3:])

            if command[0:5] == "list.":
                read(command[5:])

            elif command == "help":
                read(join('Docs', "Help"))

            elif command == "syntax":
                read(join('Docs', "syntax"))

            elif command == "changelog":
                read(join('Docs', "changelog"))


            elif command == "die" or command == "kys" or command == "exit":
                
                 end = False
            

    

        
