import random
from library import welcome_message

# Variabel
nama_game = "CAPIBARA ROOM"
nama_user = input("Masukkan Nama Kamu: ")


welcome_message("GOA CAPIBARA GAME")
print(f"Selamat Bermain {nama_user}")

# Variabel Bentuk Goa Capibara
def random_goa():
    return  random.randint(1, 4)

capibara_room = random_goa()
bentuk_goa = "|_|"
goa = [bentuk_goa] * 4

tmp_goa = goa.copy()
tmp_goa[capibara_room - 1] = "|0_0|"

goa = ' '.join(goa)
tmp_goa = ' '.join(tmp_goa)


while True:
    print(f''' 
    Hari ini di luar hujan sangat lebat, di Goa mana kah Capibara tidur?
    {goa}
    ''')

    jawaban_user = int(input("Capibara tidur di Goa Nomor [1/ 2/ 3/ 4]: "))
    if jawaban_user is not None:
        validasi = input("Apakah kamu yakin dengan jawaban kamu? [y/n]: " )
        if validasi == "n":
            continue
        elif validasi == "y" and jawaban_user == capibara_room:
            print(f'''
            Kamu Benar!
            Capibara Tidur pada goa nomor {capibara_room}
            {tmp_goa}''')
            pass
        else:
            print("Yahhh Kamu Salah!")
            coba_lagi = input("\n\n Apakah Kamu Ingin mencoba Menebaknya Lagi ? [y/n]: ")
            
            if coba_lagi == "n":
                pass
            else:
                continue
                            
            # play_again = input("\n\n Apakah Kamu Ingin Bermain Kembali ? [y/n]: ")
            # if play_again == "n":
            #     break 
                
    play_again = input("\n\n Apakah Kamu Ingin Bermain Kembali ? [y/n]: ")
    if play_again == "n":
       break 
    else:
        capibara_room = random_goa()
        

print(f"\n\n Game selesai, Capibara Lanjut bobo yaa {nama_user}")




