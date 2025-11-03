from display import tampilkan_playlist, tampilkan_musik, tampilkan_semua_data
from prettytable import PrettyTable

def tambah_musik():
        judulmusik = input("Judul Musik\t:")
        artis = input("Artis\t\t:")
        while True:
            try:
                genre = str(input("1. Klasik\n2. Pop\n3. Rock\n4. Jazz\n5. HipHop\nGenre\t\t:"))
                genre = genre.lower()
                jenis = ["klasik", "pop", "rock", "jazz", "hiphop"]
                if genre in jenis:
                    break
                else:
                    print("Pilihlah berdasrkan opsi")
            except ValueError:
                print("Hanya dalam bentuk huruf")
        while True:
            try:
                tahun = int(input("Tahun Rilis\t:"))
                if tahun >= 1950 and tahun <= 2025:
                    break
                else:
                    print("Tahun hanya dari 1950 - 2025")
            except ValueError:
                print("Tahun harus berupa angka")
        while True:
            try:
                rating = int(input("Rating Musik\t:"))
                if rating >= 1 and rating <= 5:
                    break
                else:
                    print("Rating dari 1 - 5")
            except ValueError:
                print("Rating harus berupa angka")
        return (judulmusik, artis, genre, tahun, rating)


def lihat_playlist(data, statuslogin):
    print("== Lihat Playlist ==")
    tampilkan_playlist(data, statuslogin)
    input("Tekan Enter untuk kembali...")

def tambah_playlist(data, statuslogin):
    print("== Tambah Playlist ==")
    judul = input("Judul Playlist\t: ")
    playlist = [judul, []]
    while True:
        musik = tambah_musik()
        playlist[1].append(musik)
        print("Musik berhasil ditambahkan ke playlist.")

        lanjut = input("Tambah musik lagi? (1 = Ya, lainnya = Tidak)\t: ")
        if lanjut != "1":
            break
    data[statuslogin]["playlist"].append(playlist)
    print("Playlist berhasil dibuat.", end="")
    input()
    return data

def ubah_playlist(data, statuslogin):
    print("== Ubah Playlist ==")
    if not data[statuslogin]["playlist"]:
        print("Belum ada playlist.", end="")
        input()
        return data
    
    tampilkan_playlist(data, statuslogin)
    pilih = input("Pilih judul playlist yang ingin diubah\t: ")
    for plylist in data[statuslogin]["playlist"]:
        if plylist[0] == pilih:
            print(f"\n== Ubah Playlist: {pilih} ==")
            print("1. Ubah Judul")
            print("2. Ubah Musik dalam Playlist")
            print("3. Tambahkan Musik Baru")
            opsi = input("Pilih opsi\t: ")

            if opsi == "1":
                plylist[0] = input("Judul baru\t: ")
                print("Judul playlist berhasil diubah.", end="")
            elif opsi == "2":
                if not plylist[1]:
                    print("Belum ada musik dalam playlist.", end="")
                else:
                    tampilkan_musik(plylist)
                    judullagu = input("Judul musik yang ingin diubah\t: ")
                    for idx, lagu in enumerate(plylist[1]):
                        if lagu[0] == judullagu:
                            print(f"\nMengubah musik: {lagu[0]}")
                            plylist[1][idx] = tambah_musik()
                            print("Musik berhasil diubah.", end="")
                            break
                    else:
                        print("Musik tidak ditemukan.", end="")
            elif opsi == "3":
                musik = tambah_musik()
                plylist[1].append(musik)
                print("Musik berhasil ditambahkan.", end="")
            else:
                print("Opsi tidak valid.", end="")
            input()
            return data

    print("Playlist tidak ditemukan.", end="")
    input()
    return data

def hapus_playlist(data, statuslogin):
    print("== Hapus Playlist ==")
    
    if len(data[statuslogin]["playlist"]) == 0:
        print("Belum ada playlist", end="")
        input()
        return data
    print("\n= Daftar Playlist =")
    table = PrettyTable()
    table.field_names = ["No", "Judul Playlist", "Jumlah Lagu"]
    
    for idx, plylist in enumerate(data[statuslogin]["playlist"], start=1):
        table.add_row([idx, plylist[0], len(plylist[1])])
        
    print(table)

    pilih = input("Pilih judul playlist yang ingin dihapus atau kelola\t: ")
    statusjudul = False
    
    for plylist in data[statuslogin]["playlist"]:
        if plylist[0] == pilih:
            statusjudul = True
            print("\n1. Hapus seluruh playlist")
            print("2. Hapus lagu tertentu dalam playlist")
            pilihan = input("Pilih opsi\t: ")
            
            if pilihan == "1":
                data[statuslogin]["playlist"].remove(plylist)
                print("Playlist berhasil dihapus.", end="")
                input()
                
            elif pilihan == "2":
                if len(plylist[1]) == 0:
                    print("Belum ada musik dalam playlist ini", end="")
                    input()
                else:
                    print("\n= Daftar Musik =")
                    table = PrettyTable()
                    table.field_names = ["No", "Judul Musik", "Artis", "Genre", "Tahun", "Rating"]
                    
                    for idx, lagu in enumerate(plylist[1], start=1):
                        table.add_row([idx, lagu[0], lagu[1], lagu[2], lagu[3], lagu[4]])
                    
                    print(table)
                    
                    judulmusik = input("Pilih judul musik yang ingin dihapus\t: ")
                    statusmusik = False
                    
                    for idx, lagu in enumerate(plylist[1]):
                        if lagu[0] == judulmusik:
                            statusmusik = True
                            del plylist[1][idx]
                            print("Musik berhasil dihapus", end="")
                            input()
                            break
                    
                    if not statusmusik:
                        print("Musik tidak ditemukan", end="")
                        input()
            
            else:
                print("Tidak ada aksi yang dilakukan.", end="")
                input()
            
            break
    
    if not statusjudul:
        print("Playlist tidak ditemukan.", end="")
        input()
    
    return data

def lihat_semua_data(data):
    print("== Lihat Semua Data Pengguna ==")
    tampilkan_semua_data(data)
    input("Tekan Enter untuk kembali...")

