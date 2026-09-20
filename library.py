import socket
pc_name = socket.gethostname()
from time import sleep

def welcome_message ():
    style = "*" * (len(pc_name) + 8)

    print(style)
    print(f"++* {pc_name} *++")
    print(style)

def exit_program():
    print('program di hentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program diHentikan')
    

if __name__ == '__main__':
    welcome_message()
    exit_program()