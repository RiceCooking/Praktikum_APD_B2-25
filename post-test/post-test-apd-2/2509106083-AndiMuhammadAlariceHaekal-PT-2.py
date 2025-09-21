nama = str(input("Masukkan Nama\t\t :"))
nim = int(input("Masukkan NIM\t\t :"))
dana = float(input("Masukkan Uang Belanja\t :"))

print(f"{nama} dengan NIM {nim}, ingin berbelanja dengan dana Rp.{dana}")
harga = 15000
pajakmenu = [0.05, 0.08, 0.10]
pajakPlele = harga * pajakmenu[0]
pajakMayam = harga * pajakmenu[1]
pajakNpadang = harga * pajakmenu[2]