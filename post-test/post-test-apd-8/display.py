from prettytable import PrettyTable

def tampilkan_playlist(playlists):
    for item in playlists:
        judul, lagu_list = item
        print(f"\n# Playlist: {judul}")
        if len(lagu_list) == 0:
            print("  Belum ada musik pada playlist ini.")
        else:
            table = PrettyTable()
            table.field_names = ["Judul", "Artis", "Genre", "Tahun", "Rating"]
            for lagu in lagu_list:
                table.add_row(lagu)
            print(table)
