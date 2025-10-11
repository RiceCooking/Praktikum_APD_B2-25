import os
data = [
    ["developer", "123", "Admin", []]
        ]

while True:
    os.system("cls || clear")
    print("""
=== Halaman Masuk Playlist Musik ==
1. Registrasi
2. Login
3. Keluar
""")
    opsi = input("Pilih Opsi\t:")
    if opsi == "1":
        print("Halaman Registrasi")
        usn = input("Username\t:")
        pw = input("Password\t:")
        for usn1 in data:
            if usn1[0] == usn: # kan di cek satu satu tuh dan di index 0 dari tiap element list yang ada di data, index 0 itu username
                print("Username tidak tersedia")
                break
        else:
            data.append([usn, pw, "User", []])
            print("Registrasi berhasil")
    elif opsi == "2":
        print("Halaman Login")
        usn = input("Username\t:")
        pw = input("Password\t:")
    elif opsi == "3":
        print("""
Terimakasih telah menggunakan Playlist Musik
Anda keluar dari Aplikasigit
              """)
        break