import os
from data import load_data, save_data
from auth import register, login, keluar
from playlist import lihat_playlist, tambah_playlist, 

def halaman_masuk():
    print("Beralih ke halaman masuk", end="")
    input()
    return None

data = load_data()
statuslogin = None
cek = False

while cek == False:
    os.system("cls || clear")
    print("""
=== Halaman Masuk Playlist Musik ===
1. Registrasi
2. Login
3. Keluar dari Aplikasi
""")
    try:
        opsi = int(input("Pilih Opsi\t: "))
        if opsi == 1:
            data = register(data)
            save_data(data)  
        elif opsi == 2:
            statuslogin = login(data)
        elif opsi == 3:
            cek = keluar()
        else:
            print("Pilihlah 1/2/3", end="")
            input()
            continue
    except ValueError:
        print("Input hanya berupa angka", end="")
        input()

    while statuslogin != None:
        os.system("cls || clear")
        print(f"=== Selamat Datang, {statuslogin}! ===")
        print("""
1. Lihat Playlist
2. Tambah Playlist
3. Keluar ke Menu Utama
""")
        try:
            opsi = int(input("Pilih Opsi\t: "))
            if opsi == 1:
                lihat_playlist(data, statuslogin)
            elif opsi == 2:
                data = tambah_playlist(data, statuslogin)
            elif opsi == 3:
                statuslogin = halaman_masuk()
            else:
                print("Pilihlah 1/2/3", end="")
                input()
        except ValueError:
            print("Input hanya berupa angka", end="")
            input()
save_data(data)
