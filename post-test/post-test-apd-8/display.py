from prettytable import PrettyTable

def tampilkan_playlist(data, username):
    if len(data[username]["playlist"]) == 0:
        print("Belum ada playlist untuk ditampilkan.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Judul Playlist", "Total Lagu"]

    for idx, plylist in enumerate(data[username]["playlist"], start=1):
        table.add_row([idx, plylist[0], len(plylist[1])])

    print(table)

def tampilkan_musik(plylist):
    if len(plylist[1]) == 0:
        print("Belum ada musik dalam playlist ini.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Judul", "Artis", "Genre", "Tahun", "Rating"]

    for idx, lagu in enumerate(plylist[1], start=1):
        table.add_row([idx, lagu[0], lagu[1], lagu[2], lagu[3], lagu[4]])

    print(table)
