import os
data = {
    "developer" : {
        "password" : "123",
        "role" : "admin",
        "playlist" : [],
    },
}

statuslogin = None
cek = False

def register(data):
    print("== Halaman Registrasi ==")
    usn = input("Username\t:")
    pw = input("Password\t:")
    if usn in data:
        print("Username tidak tersedia", end="")
        input()
    else:
        data[usn] = {
            "password" : pw,
            "role" : "user",
            "playlist" : [],
        }
        print("Registrasi berhasil", end="")
        input()
    return data

while cek == False:
    os.system("cls || clear")
    print("""
=== Halaman Masuk Playlist Musik ==
1. Registrasi
2. Login
3. Keluar dari Aplikasi
""")
    opsi = input("Pilih Opsi\t:")
    if opsi == "1":
        data = register(data)
    elif opsi == "2":
        print("== Halaman Login ==")
        usn = input("Username\t:")
        pw = input("Password\t:")
        if usn in data:
            if data[usn]["password"] == pw:
                print("Berhasil login",end="")
                input()
                statuslogin = usn
            else:
                print("Password salah", end="")
                input()
        else:
            print("Username tidak ditemukan", end="")
            input()
    elif opsi == "3":
        print("""
Terimakasih telah menggunakan Playlist Musik
Anda keluar dari Aplikasi
              """, end = "")
        input()
        cek = True
    else:
         print("Pilihlah 1/2/3", end="")
         input()
         continue
    while statuslogin != None:
        os.system("cls || clear")
        if data[statuslogin]["role"] == "admin":
                print("""
=== Aplikasi Playlist Musik Admin ==
1. Lihat Playlist
2. Tambah Playlist
3. Ubah Playlist
4. Hapus Playlist
5. Halaman Masuk
6. Lihat Data        
""")
                opsi = input("Opsi\t:")
                if opsi == "1":
                     print("== Lihat Playlist ==")
                     if len(data[statuslogin]["playlist"]) == 0:
                         print("Belum ada playlist", end="")
                     else:
                         print("= Daftar Playlist =")
                         for plylist in data[statuslogin]["playlist"]:
                             print(f"{plylist[0]}")
                             if len(plylist[1]) == 0:
                                 print("Belum ada musik",end="")
                             else:
                                 for lagu in plylist[1]:
                                    print(f"{lagu[0]} {lagu[1]} {lagu[2]} {lagu[3]} {lagu[4]}")
                     input()
                elif opsi == "2":
                     print("== Tambah Playlist ==")
                     judul = input("Judul Playlist\t:")
                     playlist = [judul, []]
                     while True:
                          judulmusik = input("Judul Musik\t:")
                          artis = input("Artis\t\t:")
                          while True:
                            genre = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                            genre = genre.lower()
                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                            if genre.isalpha():
                                if genre in jenis:
                                    break
                                else:
                                    print("Pilihlah berdasrkan opsi")
                            else:
                                print("Hanya dalam bentuk huruf")
                          while True:
                            tahun = str(input("Tahun Rilis\t:"))
                            if tahun.isdigit():
                                 tahun = int(tahun)
                                 if tahun >= 1950 and tahun <= 2025:
                                    tahun = str(tahun)
                                    break
                                 else:
                                      print("Tahun hanya dari 1950 - 2025")
                            else:
                                 print("Tahun harus berupa angka")
                          while True:
                            rating = str(input("Rating Musik\t:"))
                            if rating.isdigit():
                                 rating = int(rating)
                                 if rating >= 1 and rating <= 5:
                                    rating = str(rating)
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
                          opsi1 = input("Ketik 1 untuk tambahkan musik lagi\t:")
                          if opsi1 != "1":
                            print("Beralih ke halaman utama", end="")
                            input()
                            break
                     data[statuslogin]["playlist"].append(playlist)
                elif opsi == "3":
                    print("== Ubah Playlist ==")
                    if len(data[statuslogin]["playlist"]) == 0:
                        print("Belum ada playlist", end="")
                        input()
                    else:
                        print("= Daftar Playlist =")
                        for plylist in data[statuslogin]["playlist"]:
                            print(f"- {plylist[0]}")
                        pilih = input("Pilih playlist yang ingin diubah\t:")
                        statusjudul = False
                        for plylist in  data[statuslogin]["playlist"]:
                            if plylist[0] == pilih:
                                statusjudul = True
                                tanya = input("Ketik 1 untuk ubah judul playlist\t:")
                                if tanya == "1":
                                    judulbaru = input("Judul baru\t:")
                                    plylist[0] = judulbaru
                                    print("Judul playlist berhasil diubah", end ="")
                                    input()
                                elif tanya != "1":
                                    tanyamusik = input("Ketik 1 untuk ubah musik\nKetik 2 untuk tambah musik\nOpsi\t:")
                                    if tanyamusik == "1":
                                        if len(plylist[1]) == 0:
                                            print("Playlist belum ada musik",end="")
                                            input()
                                        else:
                                            print("= Daftar musik =")
                                            for lagu in plylist[1]:
                                                print(f"- {lagu[0]}")
                                            judullagu = input("Judul musik\t:")
                                            statusmusik = False
                                            for musik in range(len(plylist[1])):
                                                if plylist[1][musik][0] == judullagu:
                                                    statusmusik = True
                                                    print(f"Kamu akan mengubah musik {plylist[1][musik][0]}")
                                                    judulmusik = input("Judul Musik\t:")
                                                    artis = input("Artis\t\t:")
                                                    while True:
                                                        genre = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                                                        genre = genre.lower()
                                                        jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                                                        if genre.isalpha():
                                                            if genre in jenis:
                                                                break
                                                            else:
                                                                print("Pilihlah berdasrkan opsi")
                                                        else:
                                                            print("Hanya dalama bentuk huruf")
                                                    while True:
                                                        tahun = str(input("Tahun Rilis\t:"))
                                                        if tahun.isdigit():
                                                            tahun = int(tahun)
                                                            if tahun >= 1950 and tahun <= 2025:
                                                                tahun = str(tahun)
                                                                break
                                                            else:
                                                                print("Tahun hanya dari 1950 - 2025")
                                                        else:
                                                            print("Hanya dalam bentuk angka")
                                                    while True:
                                                        rating = str(input("Rating Musik\t:"))
                                                        if rating.isdigit():
                                                            rating = int(rating)
                                                            if rating >= 1 and rating <= 5:
                                                                rating = str(rating)
                                                                break
                                                            else:
                                                                print("Rating dari 1 - 5")
                                                        else:
                                                            print("Hanya dalam bentuk angka")
                                                    plylist[1][musik] = (judulmusik, artis, genre, tahun, rating)
                                                    print("Musik berhasil diubah", end="")
                                                    input()
                                                    break
                                            if statusmusik != True:
                                                print("Musik tidak ditemukan", end ="")
                                                input()
                                    elif tanyamusik == "2":
                                        print("= Tambah Musik =")
                                        judulmusik = input("Judul Musik\t:")
                                        artis = input("Artis\t:")
                                        while True:
                                            genre = input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:")
                                            genre = genre.lower()
                                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                                            if genre.isalpha():
                                                if genre in jenis:
                                                    break
                                                else:
                                                    print("Pilihlah berdasrkan opsi")
                                            else:
                                                print("Hanya dalam bentuk huruf")
                                        while True:
                                            tahun = str(input("Tahun Rilis\t:"))
                                            if tahun.isdigit():
                                                tahun = int(tahun)
                                                if tahun >= 1950 and tahun <= 2025:
                                                    tahun = str(tahun)
                                                    break
                                                else:
                                                    print("Tahun hanya dari 1950 - 2025")
                                            else:
                                                print("Hanya dalam bentuk angka")
                                        while True:
                                            rating = str(input("Rating Musik\t:"))
                                            if rating.isdigit():
                                                rating = int(rating)
                                                if rating >= 1 and rating <= 5:
                                                    rating = str(rating)
                                                    break
                                                else:
                                                    print("Rating dari 1 - 5")
                                            else:
                                                print("Hanya dalam bentuk angka")
                                        musikbaru = (judulmusik, artis, genre, str(tahun), str(rating))
                                        plylist[1].append(musikbaru)
                                        print("Berhasil menambahkan musik, beralih ke halaman utama", end="")
                                        input()
                                    else:
                                        print("Tidak ada yang diubah, beralih ke halaman utama", end="")
                                        input()
                                break
                        if statusjudul != True:
                            print("Playlist tidak ditemukan, beralih ke halaman utama", end="")
                            input()
                elif opsi == "4":
                    print("== Hapus Playlist ==")
                    if len(data[statuslogin]["playlist"]) == 0:
                        print("Belum ada playlist",end="")
                        input()
                    else:
                        print("= Daftar Playlist =")
                        for plylist in data[statuslogin]["playlist"]:
                            print(f"- {plylist[0]}")
                        
                        pilih = input("Pilih playlist yang ingin dihapus\t:")
                        statusjudul = False
                        for plylist in data[statuslogin]["playlist"]:
                            if plylist[0] == pilih:
                                statusjudul = True
                                pilih2 = input("Ketik 1 untuk menghapus playlist\t:")
                                if pilih2 == "1":
                                    data[statuslogin]["playlist"].remove(plylist)
                                    print("Playlist berhasil dihapus",end="")
                                    input()
                                elif pilih2 != "1":
                                    pilih3 = input("Ketik 1 untuk hapus musik dalam playlist\t:")
                                    if pilih3 == "1":
                                        if len(plylist[1]) == 0:
                                            print("Belum ada musik", end ="")
                                            input()
                                        else:
                                            print("= Daftar Musik =")
                                            for lagu in plylist[1]:
                                                print(f"- {lagu[0]}")
                                            judulmusik = input("Pilih judul musik yang ingin di hapus\t:")
                                            statusmusik = False
                                            for musik in range(len(plylist[1])):
                                                if plylist[1][musik][0] == judulmusik:
                                                    statusmusik = True
                                                    del plylist[1][musik]
                                                    print("Musik berhasil dihapus", end="")
                                                    input()
                                                    break
                                            if statusmusik != True:
                                                print("Musik tidak ditemukan", end="")
                                                input()
                                    else:
                                        print("Tidak menghapus apapun, beralih ke halaman utama",end="")
                                        input()
                                break
                        if statusjudul != True:
                            print("Playlist tidak ditemukan, beralih kehalaman menu", end="")
                            input()
                elif opsi == "5":
                     print("Beralih ke halaman masuk", end ="")
                     input()
                     statuslogin = None
                elif opsi == "6":
                    print("== Lihat Data ==")
                    for akun, bio in data.items():
                        print(akun, bio)
                    input()
                else:
                     print("Pilihlah 1/2/3/4/5/6", end="")
                     input()
                     continue
        elif data[statuslogin]["role"] == "user":
                print("""
=== Aplikasi Playlist Musik ==
1. Lihat Playlist
2. Tambah Playlist
3. Ubah Playlist
4. Hapus Playlist
5. Halaman Masuk 
""")
                opsi = input("Opsi\t:")
                if opsi == "1":
                     print("== Lihat Playlist ==")
                     if len(data[statuslogin]["playlist"]) == 0:
                         print("Belum ada playlist", end="")
                     else:
                         print("= Daftar Playlist =")
                         for plylist in data[statuslogin]["playlist"]:
                             print(f"{plylist[0]}")
                             if len(plylist[1]) == 0:
                                 print("Belum ada musik",end="")
                             else:
                                 for lagu in plylist[1]:
                                    print(f"{lagu[0]} {lagu[1]} {lagu[2]} {lagu[3]} {lagu[4]}")
                     input()
                elif opsi == "2":
                     print("== Tambah Playlist ==")
                     judul = input("Judul Playlist\t:")
                     playlist = [judul, []]
                     while True:
                          judulmusik = input("Judul Musik\t:")
                          artis = input("Artis\t\t:")
                          while True:
                            genre = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                            genre = genre.lower()
                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                            if genre.isalpha():
                                if genre in jenis:
                                    break
                                else:
                                    print("Pilihlah berdasrkan opsi")
                            else:
                                print("Hanya dalam bentuk huruf")
                          while True:
                            tahun = str(input("Tahun Rilis\t:"))
                            if tahun.isdigit():
                                 tahun = int(tahun)
                                 if tahun >= 1950 and tahun <= 2025:
                                    tahun = str(tahun)
                                    break
                                 else:
                                      print("Tahun hanya dari 1950 - 2025")
                            else:
                                 print("Tahun harus berupa angka")
                          while True:
                            rating = str(input("Rating Musik\t:"))
                            if rating.isdigit():
                                 rating = int(rating)
                                 if rating >= 1 and rating <= 5:
                                    rating = str(rating)
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
                          opsi1 = input("Ketik 1 untuk tambahkan musik lagi\t:")
                          if opsi1 != "1":
                            print("Beralih ke halaman utama", end="")
                            input()
                            break
                     data[statuslogin]["playlist"].append(playlist)
                elif opsi == "3":
                    print("== Ubah Playlist ==")
                    if len(data[statuslogin]["playlist"]) == 0:
                        print("Belum ada playlist", end="")
                        input()
                    else:
                        print("= Daftar Playlist =")
                        for plylist in data[statuslogin]["playlist"]:
                            print(f"- {plylist[0]}")
                        pilih = input("Pilih playlist yang ingin diubah\t:")
                        statusjudul = False
                        for plylist in  data[statuslogin]["playlist"]:
                            if plylist[0] == pilih:
                                statusjudul = True
                                tanya = input("Ketik 1 untuk ubah judul playlist\t:")
                                if tanya == "1":
                                    judulbaru = input("Judul baru\t:")
                                    plylist[0] = judulbaru
                                    print("Judul playlist berhasil diubah", end ="")
                                    input()
                                elif tanya != "1":
                                    tanyamusik = input("Ketik 1 untuk ubah musik\nKetik 2 untuk tambah musik\nOpsi\t:")
                                    if tanyamusik == "1":
                                        if len(plylist[1]) == 0:
                                            print("Playlist belum ada musik",end="")
                                            input()
                                        else:
                                            print("= Daftar musik =")
                                            for lagu in plylist[1]:
                                                print(f"- {lagu[0]}")
                                            judullagu = input("Judul musik\t:")
                                            statusmusik = False
                                            for musik in range(len(plylist[1])):
                                                if plylist[1][musik][0] == judullagu:
                                                    statusmusik = True
                                                    print(f"Kamu akan mengubah musik {plylist[1][musik][0]}")
                                                    judulmusik = input("Judul Musik\t:")
                                                    artis = input("Artis\t\t:")
                                                    while True:
                                                        genre = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                                                        genre = genre.lower()
                                                        jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                                                        if genre.isalpha():
                                                            if genre in jenis:
                                                                break
                                                            else:
                                                                print("Pilihlah berdasrkan opsi")
                                                        else:
                                                            print("Hanya dalama bentuk huruf")
                                                    while True:
                                                        tahun = str(input("Tahun Rilis\t:"))
                                                        if tahun.isdigit():
                                                            tahun = int(tahun)
                                                            if tahun >= 1950 and tahun <= 2025:
                                                                tahun = str(tahun)
                                                                break
                                                            else:
                                                                print("Tahun hanya dari 1950 - 2025")
                                                        else:
                                                            print("Hanya dalam bentuk angka")
                                                    while True:
                                                        rating = str(input("Rating Musik\t:"))
                                                        if rating.isdigit():
                                                            rating = int(rating)
                                                            if rating >= 1 and rating <= 5:
                                                                rating = str(rating)
                                                                break
                                                            else:
                                                                print("Rating dari 1 - 5")
                                                        else:
                                                            print("Hanya dalam bentuk angka")
                                                    plylist[1][musik] = (judulmusik, artis, genre, tahun, rating)
                                                    print("Musik berhasil diubah", end="")
                                                    input()
                                                    break
                                            if statusmusik != True:
                                                print("Musik tidak ditemukan", end ="")
                                                input()
                                    elif tanyamusik == "2":
                                        print("= Tambah Musik =")
                                        judulmusik = input("Judul Musik\t:")
                                        artis = input("Artis\t:")
                                        while True:
                                            genre = input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:")
                                            genre = genre.lower()
                                            jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                                            if genre.isalpha():
                                                if genre in jenis:
                                                    break
                                                else:
                                                    print("Pilihlah berdasrkan opsi")
                                            else:
                                                print("Hanya dalam bentuk huruf")
                                        while True:
                                            tahun = str(input("Tahun Rilis\t:"))
                                            if tahun.isdigit():
                                                tahun = int(tahun)
                                                if tahun >= 1950 and tahun <= 2025:
                                                    tahun = str(tahun)
                                                    break
                                                else:
                                                    print("Tahun hanya dari 1950 - 2025")
                                            else:
                                                print("Hanya dalam bentuk angka")
                                        while True:
                                            rating = str(input("Rating Musik\t:"))
                                            if rating.isdigit():
                                                rating = int(rating)
                                                if rating >= 1 and rating <= 5:
                                                    rating = str(rating)
                                                    break
                                                else:
                                                    print("Rating dari 1 - 5")
                                            else:
                                                print("Hanya dalam bentuk angka")
                                        musikbaru = (judulmusik, artis, genre, str(tahun), str(rating))
                                        plylist[1].append(musikbaru)
                                        print("Berhasil menambahkan musik, beralih ke halaman utama", end="")
                                        input()
                                    else:
                                        print("Tidak ada yang diubah, beralih ke halaman utama", end="")
                                        input()
                                break
                        if statusjudul != True:
                            print("Playlist tidak ditemukan, beralih ke halaman utama", end="")
                            input()
                elif opsi == "4":
                    print("== Hapus Playlist ==")
                    if len(data[statuslogin]["playlist"]) == 0:
                        print("Belum ada playlist",end="")
                        input()
                    else:
                        print("= Daftar Playlist =")
                        for plylist in data[statuslogin]["playlist"]:
                            print(f"- {plylist[0]}")
                        
                        pilih = input("Pilih playlist yang ingin dihapus\t:")
                        statusjudul = False
                        for plylist in data[statuslogin]["playlist"]:
                            if plylist[0] == pilih:
                                statusjudul = True
                                pilih2 = input("Ketik 1 untuk menghapus playlist\t:")
                                if pilih2 == "1":
                                    data[statuslogin]["playlist"].remove(plylist)
                                    print("Playlist berhasil dihapus",end="")
                                    input()
                                elif pilih2 != "1":
                                    pilih3 = input("Ketik 1 untuk hapus musik dalam playlist\t:")
                                    if pilih3 == "1":
                                        if len(plylist[1]) == 0:
                                            print("Belum ada musik", end ="")
                                            input()
                                        else:
                                            print("= Daftar Musik =")
                                            for lagu in plylist[1]:
                                                print(f"- {lagu[0]}")
                                            judulmusik = input("Pilih judul musik yang ingin di hapus\t:")
                                            statusmusik = False
                                            for musik in range(len(plylist[1])):
                                                if plylist[1][musik][0] == judulmusik:
                                                    statusmusik = True
                                                    del plylist[1][musik]
                                                    print("Musik berhasil dihapus", end="")
                                                    input()
                                                    break
                                            if statusmusik != True:
                                                print("Musik tidak ditemukan", end="")
                                                input()
                                    else:
                                        print("Tidak menghapus apapun, beralih ke halaman utama",end="")
                                        input()
                                break
                        if statusjudul != True:
                            print("Playlist tidak ditemukan, beralih kehalaman menu", end="")
                            input()
                elif opsi == "5":
                     print("Beralih ke halaman masuk", end ="")
                     input()
                     statuslogin = None
                else:
                    print("Pilihlah opsi 1/2/3/4/5", end="")
                    input()