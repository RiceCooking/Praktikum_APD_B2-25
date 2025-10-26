import os
def faktorial(n):
    if n == 0 or n <1:
        return 1
    else:
        return n * faktorial(n-1)
    
while True:
    os.system("cls || clear")
    try:
        bil = int(input("Masukkan angka\t\t:"))
        print(f"Faktorial dari {bil}\t:{faktorial(bil)}", end="")
        input()
        break
    except ValueError:
        print("Input hanya berupa angka", end="")
        input()
        continue
    finally:
        print("selesai", end="")
        input()

# # def p():
# #     h = "hahaha"
# #     print(h)
# # p()
# #jika def meiliki "return" -> fungsi jika tidak ada -> prosuder
# def menu():
#     print("=== Menu Utama ===")
#     print("1. Tambah Data")
#     print("2. Hapus Data")
#     print("3. Tampilkan Data")
#     print("4. Keluar")
#     pilihan = input("Pilih menu (1-4): ")
#     return pilihan

# def tambah_data():
#     print("Menambahkan data")
#     print("Data berhasil ditambahkan", end="")
    
# def hapus_data():
#     print("Menghapus data")
#     print("Data berhasil dihapus", end="")

# def tampilkan_data():
#     print("Menampilkan data")
#     print("Data ditampilkan", end="")

# while True:
#     os.system("cls || clear")
#     pilihan = menu()
#     if pilihan == '1':
#         print(f"{tambah_data()}",end="")
#         input()
#     elif pilihan == '2':
#         print(f"{hapus_data()}",end="")
#         input()
#     elif pilihan == '3':
#         print(f"{tampilkan_data()}",end="")
#         input()
#     elif pilihan == '4':
#         print("Keluar dari program", end="")
#         input()
#         break
#     else:
#         print("Pilihan tidak valid, silakan coba lagi.", end="")
#         input()

        
        
# def l():
#     luas = 1
#     print(luas)
#     return luas

# print(l())
# print("")
# l()