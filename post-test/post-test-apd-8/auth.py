# auth.py
def register(data):
    print("== Halaman Registrasi ==")
    usn = input("Username\t: ")
    pw = input("Password\t: ")
    if usn in data:
        print("Username tidak tersedia", end="")
        input()
    else:
        data[usn] = {
            "password": pw,
            "role": "user",
            "playlist": [],
        }
        print("Registrasi berhasil", end="")
        input()
    return data

def login(data):
    print("== Halaman Login ==")
    usn = input("Username\t: ")
    pw = input("Password\t: ")
    if usn in data:
        if data[usn]["password"] == pw:
            print("Berhasil login", end="")
            input()
            return usn
        else:
            print("Password salah", end="")
            input()
    else:
        print("Username tidak ditemukan", end="")
        input()
    return None

def keluar():
    print("""
Terimakasih telah menggunakan Playlist Musik
Anda keluar dari Aplikasi
""", end="")
    input()
    return True

