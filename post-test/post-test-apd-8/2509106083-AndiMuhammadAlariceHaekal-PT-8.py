import os
from auth import register, login, keluar
from playlist import lihat_playlist, tambah_playlist, ubah_playlist, hapus_playlist, lihat_semua_data, halaman_masuk
from data import load_data, save_data

def menu_admin(data, statuslogin):
    while True:
        os.system("cls || clear")
        print("""
=== Aplikasi Playlist Musik Admin ==
1. Lihat Playlist
2. Tambah Playlist
3. Ubah Playlist
4. Hapus Playlist
5. Halaman Masuk
6. Lihat Semua Data
""")
        try:
            opsi = int(input("Opsi\t:"))
            if opsi == 1:
                lihat_playlist(data, statuslogin)
            elif opsi == 2:
                data = tambah_playlist(data, statuslogin)
            elif opsi == 3:
                data = ubah_playlist(data, statuslogin)
            elif opsi == 4:
                data = hapus_playlist(data, statuslogin)
            elif opsi == 5:
                statuslogin = halaman_masuk()
                return statuslogin 
            elif opsi == 6:
                lihat_semua_data(data)
            else:
                print("Pilihlah 1/2/3/4/5/6", end="")
                input()
        except ValueError:
            print("Input hanya berupa angka.", end="")
            input()
        save_data(data)

def menu_user(data, statuslogin):
    while True:
        os.system("cls || clear")
        print("""
=== Aplikasi Playlist Musik ==
1. Lihat Playlist
2. Tambah Playlist
3. Ubah Playlist
4. Hapus Playlist
5. Halaman Masuk
""")
        try:
            opsi = int(input("Opsi\t:"))
            if opsi == 1:
                lihat_playlist(data, statuslogin)
            elif opsi == 2:
                data = tambah_playlist(data, statuslogin)
            elif opsi == 3:
                data = ubah_playlist(data, statuslogin)
            elif opsi == 4:
                data = hapus_playlist(data, statuslogin)
            elif opsi == 5:
                statuslogin = halaman_masuk()
                return statuslogin 
            else:
                print("Pilihlah 1/2/3/4/5", end="")
                input()
        except ValueError:
            print("Input hanya berupa angka.", end="")
            input()
        save_data(data)

def main():
    data = load_data()
    statuslogin = None
    cek = False

    while not cek:
        os.system("cls || clear")
        print("""
=== Halaman Masuk Playlist Musik ===
1. Registrasi
2. Login
3. Keluar dari Aplikasi
""")
        try:
            opsi = int(input("Pilih Opsi\t:"))
            if opsi == 1:
                data = register(data)
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

        if statuslogin:
            if data[statuslogin]["role"] == "admin":
                statuslogin = menu_admin(data, statuslogin)
            else:
                statuslogin = menu_user(data, statuslogin)

if __name__ == "__main__":
    main()
