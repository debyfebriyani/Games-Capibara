from library import welcome_message, exit_program
from games import capibara
from tools import warung

def options():
    while True:
        options_menu = int(input('\n\nProgram Menu : \n1. Game Tebak Goa Capibara \n2. Aplikasi WARUNG \n3. Keluar Program \nSilahkan pilih program menu : '))
        if options_menu == 1:
            capibara.start()
        elif options_menu == 2:
            warung.start()
        elif options_menu == 3:
            exit_program()
            break
        else:
            print("Hanya bisa memilih menu yang tersedia!")

def main():
    welcome_message()
    options()

if __name__ == '__main__':
    main()