import random
import main

# Variabel Bentuk Goa Capibara
def random_goa():
    return  random.randint(1, 4)



def start():
    while True:
        capibara_room = random_goa()
        bentuk_goa = "|_|"
        goa = [bentuk_goa] * 4

        tmp_goa = goa.copy()
        tmp_goa[capibara_room - 1] = "|0_0|"

        goa = ' '.join(goa)
        tmp_goa = ' '.join(tmp_goa)


        print(f'\n\nHari ini di luar hujan sangat lebat, di Goa mana kah Capibara tidur? \n{goa}\n')

        jawaban_user = int(input("Capibara tidur di Goa Nomor [1/ 2/ 3/ 4]: "))
        if jawaban_user == capibara_room:
            print(f'\n\nKamu BENAR! \nCapibara Tidur pada goa nomor {capibara_room} \n{tmp_goa}\n')
            pass
        else:
            print("Yahhh Kamu Salah!")

                                            
        play_again = input('\n\n Apakah Kamu Ingin Bermain Kembali ? [y/n]: ')
        if play_again == "n":
            main.options() 
        else:
            capibara_room = random_goa()
            

print(f'\n\n Game selesai, Capibara Lanjut bobo yaa \n')

if __name__ == '__main__':
    start()