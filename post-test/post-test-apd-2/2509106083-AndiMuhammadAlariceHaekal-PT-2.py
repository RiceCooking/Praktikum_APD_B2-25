print("========= Selamat Datang =========")
nama = str(input("Masukkan Nama\t\t :"))
nim = int(input("Masukkan NIM\t\t :"))
harga = float(input("Masukkan Uang Belanja\t :"))

pajakPlele = float(harga * 0.05)
pajakMayam = float(harga * 0.08)
pajakNpadang = float(harga * 0.10)

totalPlele = float(harga + pajakPlele)
totalMayam = float(harga + pajakMayam)
totalNpadang = float(harga + pajakNpadang)

print(f"\n{nama} dengan NIM {nim}, ingin berbelanja dengan uang Rp{harga}.")
print("""\n.-,--.         .           ,.   .-,--. ,-_/ ,---. 
 `|__/ ,-. ,-. |- ,-.     / |    `|__/ '  | |  -' 
  | \  |-' `-. |  | |    /~~|-.   | \  .- | |  -. 
`-'  ` `-' `-' `' `-'  ,'   `-' `-'  ` `--' `---' 
                                                   """)
print(f"|==================MENU==================|")
print(f"|---Makanan----Pajak---------Harga-------|")
print(f"| Pecel Lele  | 5%  |   Rp{totalPlele}   |")
print(f"|  Mie  Ayam  | 8%  |   Rp{totalMayam}   |")
print(f"| Nasi Padang | 10% |  Rp{totalNpadang}  |")
print(f"|========================================|")