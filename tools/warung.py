import main

def start():
    while True:
        print("Ini adalah aplikasi WARUNG")
        total_belanja = int(input("Masukkan total belanja : "))

        if total_belanja == 0 :
             main.options()

if __name__ == '__main__':
    start()