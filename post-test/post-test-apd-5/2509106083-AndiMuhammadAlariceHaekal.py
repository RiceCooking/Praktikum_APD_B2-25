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
Anda keluar dari Aplikasi
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
5. Kelola Data         
""")
                opsi = input("Opsi\t:")
                if opsi == "1":
                     print("== Lihat Playlist ==")
                     if len(user[3]) == 0:
                         print("Belum ada playlist", end="")
                         input()
                     else:
                         print("= Daftar Playlist =")
                         for plylist in user[3]:
                             print(f"{plylist[0]}")
                             if len(plylist[1]) == 0:
                                 print("Belum ada musik")
                             else:
                                 for lagu in plylist[1]:
                                    print(f"{lagu[0]} {lagu[1]} {lagu[2]} {lagu[3]} {lagu[4]}", end ="")
                                    input()
                elif opsi == "2":
                     print("== Tambah Playlist ==")
                     judul = "Playlist : "
                     judul1 = input("Judul Playlist\t:")
                     judul += judul1
                     playlist = [judul, []]
                     while True:
                          judulmusik = "Judul Musik : "
                          judulmusik1 = input("Judul Musik\t:")
                          judulmusik += judulmusik1
                          while True:
                            genre = "Genre : "
                            genre1 = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                            genre1 = genre1.lower()
                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                            if genre1.isalpha():
                                if genre1 in jenis:
                                    genre += genre1
                                    break
                                else:
                                    print("Pilihlah berdasrkan opsi")
                            else:
                                print("Hanya dalam bentuk huruf")
                          artis = "Artis : "
                          artis1 = input("Artis\t\t:")
                          artis += artis1
                          while True:
                            tahun = str("Tahun Rilis : ")
                            tahun1 = str(input("Tahun Rilis\t:"))
                            if tahun1.isdigit():
                                 tahun1 = int(tahun1)
                                 if tahun1 >= 1950 and tahun1 <= 2025:
                                    tahun1 = str(tahun1)
                                    tahun += tahun1
                                    break
                                 else:
                                      print("Tahun hanya dari 1950 - 2025")
                            else:
                                 print("Tahun harus berupa angka")
                          while True:
                            rating = "Rating Musik : "
                            rating1 = str(input("Rating Musik\t:"))
                            if rating1.isdigit():
                                 rating1 = int(rating1)
                                 if rating1 >= 1 and rating1 <= 5:
                                    rating1 = str(rating1)
                                    rating += rating1
                                    break
                                 else:
                                      print("Rating dari 1 - 5")
                            else:
                                 print("Rating harus berupa angka")
                          musik = (judulmusik, artis, str(genre), str(tahun), str(rating))
                          playlist[1].append(musik)
                          print("""Playlist berhasil di tambahkan """)
                          print(playlist)
                          input()
                          opsi1 = input("""
Ketik 1 untuk tambahkan musik lagi
""")
                          if opsi1 != "1":
                            print("Beralih ke halaman utama", end="")
                            input()
                            break
                     user[3].append(playlist)
                elif opsi == "3":
                    print("== Ubah Playlist ==")
                    if len(user[3]) == 0:
                        print("Belum ada playlist", end="")
                        input()
                    else:
                        print("= Daftar Playlist =", end="")
                        for plylist in user[3]:
                            print(f"- {plylist[0]}")
                            pilih = input("Pilih playlist yang ingin diubah\t:")
                            statusjudul = False
                            if plylist[0] == pilih:
                                statusjudul = True
                                tanya = input("Ketik 1 untuk ubah judul playlist\t:")
                                if tanya == "1":
                                    judulbaru = input("Judul baru\t:")
                                    plylist[0] = judulbaru
                                    print("Judul playlist berhasil diubah")
                                elif tanya != "1":
                                    tanyamusik = input("Ketik 1 untuk ubah musik")
                                    if tanyamusik == "1":
                                        if len(plylist[1]) == 0:
                                            print("Playlist belum ada musik")
                                        else:
                                            print("= Daftar musik =")
                                            for lagu in plylist[1]:
                                                print(f"= {lagu[0]}")
                                                judullagu = input("Tulis judul lagunya\t:")
                                                statusmusik = False
                                                for musik in range(len(plylist[1])):
                                                    if plylist[1][musik][0] == judullagu:
                                                        statusmusik = True
                                                        print(f"Kamu akan mengubah musik{plylist[1][musik][0]}")
                                                        judulmusik = "Judul musik : "
                                                        judulmusik1 = input("Judul Musik\t:")
                                                        judulmusik += judulmusik1
                                                        artis = "Artis : "
                                                        artis1 = input("Artis\t\t:")
                                                        artis += artis1
                                                        while True:
                                                            genre = "Genre : "
                                                            genre1 = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                                                            genre1 = genre1.lower()
                                                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                                                            if genre1.isalpha():
                                                                if genre1 in jenis:
                                                                    genre += genre1
                                                                    break
                                                                else:
                                                                    print("Pilihlah berdasrkan opsi")
                                                            else:
                                                                print("Hanya dalama bentuk huruf")
                                                        while True:
                                                            tahun = str("Tahun Rilis : ")
                                                            tahun1 = str(input("Tahun Rilis\t:"))
                                                            if tahun1.isdigit():
                                                                tahun1 = int(tahun1)
                                                                if tahun1 >= 1950 and tahun1 <= 2025:
                                                                    tahun1 = str(tahun1)
                                                                    tahun += tahun1
                                                                    break
                                                                else:
                                                                    print("Tahun hanya dari 1950 - 2025")

                                                            else:
                                                                print("Hanya dalam bentuk angka")
                                                        while True:
                                                            rating = str("Rating Musik : ")
                                                            rating1 = str(input("Rating Musik : "))
                                                            if rating1.isdigit():
                                                                rating1 = int(rating1)
                                                                if rating1 >= 1 and rating1 <= 5:
                                                                    rating1 = str(rating1)
                                                                    rating += rating1
                                                                    break
                                                                else:
                                                                    print("Rating dari 1 - 5")
                                                            else:
                                                                print("Hanya dalam bentuk angka")
                                                        plylist[1][musik] = (judulmusik, artis, genre, tahun, rating)
                                                        print("Lagu berhasil diubah")
                                                        break
                                                    

                                                if statusmusik != True:
                                                    print("Lagu tidak ditemukan")
                                    else:
                                        print("Tidak ada yang diubah, beralih ke menu utama")
                                        break
                            elif statusjudul != True:
                                print("Playlist tidak ditemukan, beralih ke halaman utama", end="")
                                input()
                elif opsi == "4":
                     print("Beralih ke halaman masuk", end ="")
                     input()
                     statuslogin = None
                elif opsi == "5":
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
""")
                opsi = input("Opsi\t:")
                if opsi == "1":
                     print("== Lihat Playlist ==", end="")
                     input()
                     if len(user[3]) == 0:
                         print("Belum ada playlist", end="")
                         input()
                     else:
                         print("= Daftar Playlist =")
                         for plylist in user[3]:
                             print(f"{plylist[0]}")
                             for lagu in plylist[1]:
                                 print(f"{lagu[0]} {lagu[1]} {lagu[2]} {lagu[3]} {lagu[4]}", end ="")
                                 input()
                elif opsi == "2":
                     print("== Tambah Playlist ==")
                     judul = "Playlist : "
                     judul1 = input("Judul Playlist\t:")
                     judul += judul1
                     playlist = [judul, []]
                     while True:
                          judulmusik = "Judul Musik : "
                          judulmusik1 = input("Judul Musik\t:")
                          judulmusik += judulmusik1
                          while True:
                            genre = "Genre : "
                            genre1 = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                            genre1 = genre1.lower()
                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                            if genre1.isalpha():
                                if genre1 in jenis:
                                    genre += genre1
                                    break
                                else:
                                    print("Pilihlah berdasrkan opsi", end="")
                                    input()
                            else:
                                print("Hanya dalam bentuk huruf", end="")
                                input()
                          artis = "Artis : "
                          artis1 = input("Artis\t\t:")
                          artis += artis1
                          while True:
                            tahun = str("Tahun Rilis : ")
                            tahun1 = str(input("Tahun Rilis\t:"))
                            if tahun1.isdigit():
                                 tahun1 = int(tahun1)
                                 if tahun1 >= 1950 and tahun1 <= 2025:
                                    tahun1 = str(tahun1)
                                    tahun += tahun1
                                    break
                                 else:
                                      print("Tahun hanya dari 1950 - 2025", end="")
                                      input()
                            else:
                                 print("Tahun harus berupa angka", end="")
                                 input()
                          while True:
                            rating = "Rating Musik : "
                            rating1 = str(input("Rating Musik\t:"))
                            if rating1.isdigit():
                                 rating1 = int(rating1)
                                 if rating1 >= 1 and rating1 <= 5:
                                    rating1 = str(rating1)
                                    rating += rating1
                                    break
                                 else:
                                      print("Rating dari 1 - 5", end="")
                                      input()
                            else:
                                 print("Rating harus berupa angka", end="")
                                 input()
                          musik = (judulmusik, artis, str(genre), str(tahun), str(rating))
                          playlist[1].append(musik)
                          print("""Playlist berhasil di tambahkan """)
                          print(playlist)
                          input()
                          opsi1 = input("""
Ketik 1 untuk tambahkan musik lagi
""")
                          if opsi1 != "1":
                            print("Beralih ke halaman utama", end="")
                            input()
                            break
                     user[3].append(playlist)
                     user
                elif opsi == "3":
                     user
                elif opsi == "4":
                     print("Beralih ke halaman masuk", end ="")
                     input()
                     statuslogin = None
                else:
                     print("Pilihlah 1/2/3/4", end="")
                     input()
                     continue