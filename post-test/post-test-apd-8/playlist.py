from display import tampilkan_playlist
from data import save_data

def lihat_playlist(data, statuslogin):
    print("== Lihat Playlist ==")
    if len(data[statuslogin]["playlist"]) == 0:
        print("Belum ada playlist", end="")
    else:
        tampilkan_playlist(data[statuslogin]["playlist"])
    input()

def tambah_musik():
    judul = input("Judul Musik\t: ")
    artis = input("Artis\t\t: ")
    genre = input("Genre\t\t: ").lower()
    tahun = int(input("Tahun Rilis\t: "))
    rating = int(input("Rating Musik\t: "))
    return (judul, artis, genre, tahun, rating)

def tambah_playlist(data, statuslogin):
    print("== Tambah Playlist ==")
    judul_playlist = input("Judul Playlist\t: ")
    playlist = [judul_playlist, []]
    while True:
        musik = tambah_musik()
        playlist[1].append(musik)
        print("Musik berhasil ditambahkan ke playlist.")
        opsi = input("Tambah musik lagi? (y/n): ")
        if opsi.lower() != 'y':
            break
    data[statuslogin]["playlist"].append(playlist)
    save_data(data)
    print("Playlist berhasil disimpan!", end="")
    input()
    return data
