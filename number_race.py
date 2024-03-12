from random import randint
import os

menu_status = True
opt_status = True
#Functions
def main_menu():

    while menu_status:
        global opt_status
        global menu_status
        os.system('clear')
        print("::: MAIN MENU :::")
        print("[1]. Play")
        print("[2]. Help")
        print("[3]. About us")
        print("[4]. Exit")

    while opt_status:
        opt = input(".:::Press any option: ")
        if opt < 1 or opt > 4
        print(":::Invalid option, try again:::")
        else:
            opt_status = False
    
    if opt == '4':
        break
#Main
os.system('clear')
print('Loading...')
key = input(":::.Press any key to continue.:::")
main_menu()

