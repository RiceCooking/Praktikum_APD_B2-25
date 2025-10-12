import os
data = [
    ["developer", "123", "Admin", []]
        ]

statuslogin = None

while True:
    os.system("cls || clear")
    print("""
=== Halaman Masuk Playlist Musik ==
1. Registrasi
2. Login
3. Keluar dari Aplikasi
""")
    opsi = input("Pilih Opsi\t:")
    if opsi == "1":
        print("Halaman Registrasi")
        usn = input("Username\t:")
        pw = input("Password\t:")
        for usn1 in data:
            if usn1[0] == usn: # kan di cek satu satu tuh dan di index 0 dari tiap element list yang ada di data, index 0 itu username
                print("Username tidak tersedia", end = "")
                input()
                break
        else:
            data.append([usn, pw, "User", []])
            print("Registrasi berhasil", end="")
            input()
    elif opsi == "2":
        print("Halaman Login")
        usn = input("Username\t:")
        pw = input("Password\t:")
        user = None
        for usn1 in data:
            if usn1[0] == usn:
                user = usn1
                break
        if user != None:
            if user[1] == pw:
                print("Login berhasil", end="")
                statuslogin = user
                input()
            else:
                print("Password salah", end="")
                input()
        else:
            print("Username tidak ditemukan",end="")
            input()
            continue
    
 #alur logika kan awalnya user ga ada nilainya terus di cek satu satu di data, setiap usn1 ada pada elemen data. terus kalau ketemu, usernamenya itu jadi nilainya user
 #karene ketemu bearti kan list data pengguna tuh kan adalah elemen di data dlm bentuk list jadi pas bener tuh otomatis satu elemen yg benar itu yang dibaca sama program 
 #nah karena user = elemen yg usernamenya bener, cek lagi pwnya di index ke 1 kalau sama bearti syrat loginnya terpenuhi tpi perlu di simpan lgi data si userny
 #caranya statuslogin yg awalny g ad nilai jadi dimasukkan nilai si user tadi, dimana nilai user itu ada elemen dari data jadi 
    elif opsi == "3":
        print("""
Terimakasih telah menggunakan Playlist Musik
Anda keluar dari Aplikasigit
              """, end = "")
        input()
        break
    else:
         print("Pilihlah 1/2/3", end="")
         input()
         continue
    while statuslogin != None:
        os.system("cls || clear")
        if user[2] == "Admin":
                print("""
=== Aplikasi Playlist Musik Admin ==
1. Lihat Playlist
2. Tambah Playlist
3. Ubah Playlist
4. Halaman Login
5. Keluar dari Aplikasi
6. Kelola Data         
""")
                opsi = input("Opsi\t:")
                if opsi == "1":
                     user
                elif opsi == "2":
                     print("== Tambah Playlist ==")
                     judul = input()
                     playlist = [judul, []]
                     while True:
                          judulmusik = input("Judul Musik\t:")
                          genre = input("Genre\t\t:")
                          artis = input("Artis\t\t:")
                          while True:

                            os.system("cls || clear")
                            tahun = str(input("Tahun Rilis\t:"))
                            if tahun.isdigit():
                                 tahun = int(tahun)
                                 if tahun >= 1950 and tahun <= 2025:
                                    break
                                 else:
                                      print("Tahun hanya dari 1950 - 2025", end="")
                                      input()
                            else:
                                 print("Tahun harus berupa angka", end="")
                                 input()
                          while True:
                            os.system("cls || clear")
                            rating = str(input("Rating Musik\t:"))
                            if rating.isdigit():
                                 rating = int(rating)
                                 if rating >= 1 and rating <= 5:
                                    break
                                 else:
                                      print("Rating dari 1 - 5", end="")
                                      input()
                            else:
                                 print("Rating harus berupa angka", end="")
                                 input()
                            musik = (judulmusik, artis, genre, str(tahun), str(rating))
                            playlist[1].append(musik)
                            print("""Playlist berhasil di tambahkan """)
                            input()
                            print(playlist)
                            input()
                            statuslogin = None
                            break

                elif opsi == "3":
                     user
                elif opsi == "4":
                     user
                elif opsi == "5":
                     user
                elif opsi == "6":
                     user
                else:
                     print("Pilihlah 1/2/3/4/5/6", end="")
                     input()
                     continue
        elif user[2] == "User":
                print("""
=== Aplikasi Playlist Musik ==
1. Lihat Playlist
2. Tambah Playlist
3. Ubah Playlist
4. Halaman Masuk
5. Keluar dari Aplikasi      
""")
                opsi = input("Opsi\t:")
                if opsi == "1":
                     user
                elif opsi == "2":
                     user
                elif opsi == "3":
                     user
                elif opsi == "4":
                     user
                elif opsi == "5":
                     user
                else:
                     print("Pilihlah 1/2/3/4/5", end="")
                     input()
                     continue