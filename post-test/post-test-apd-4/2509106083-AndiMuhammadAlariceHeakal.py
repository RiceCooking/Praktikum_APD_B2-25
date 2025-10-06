# Buatlah program Python untuk program Toko Furnitur Infordeh.

# 1. Validasi Login:
# Gunakan nama sebagai username dan NIM sebagai password.
# Batas percobaan login maksimal 3 kali.
# Jika login gagal 3 kali, program akan berhenti dan tidak menampilkan menu pembelian furnitur.
# Jika login berhasil, program menampilkan menu pembelian furnitur.

# 2. Menu Pembelian Tiket
# Tampilan menu pembelian furnitur harus terdapat opsi berikut:
# opsi 1 -> Sofa dengan Harga per unit Rp 500.000
# opsi 2 -> Meja Belajar dengan Harga per unit Rp.250.000
# opsi 3 -> Rak lemari dengan Harga per unit Rp.150.000
# opsi 4 -> Keluar dari program

# Setelah pengguna memilih opsi furnitur, maka program akan meminta input jumlah furnitur yang ingin dibeli.
# Menu akan terus muncul sampai pengguna memilih Keluar.

# 3. Tampilan Hasil
# Hitung total bayar dengan menggunakan for (looping sesuai jumlah unit).
# Tampilkan hasil berupa jenis unit yang dipilih, jumlah unit dan total bayar.

# 4. POIN PLUS (+)
# Tambahkan ketentuan,
# Jika total bayar >= Rp.700.000, maka ia mendapat potongan 20% dari total bayar akhir.
# Jika total bayar >= Rp.500.000 dan total bayar < Rp.700.000, maka ia mendapat potongan 8% dari total bayar akhir.
# Jika total bayar >= Rp.150.000 dan < Rp.500.000, maka ia mendapat Kitchen Set.
# Terapkan error handling sederhana menggunakan if/else tanpa try-except.
nama = "Haekal"
nim = "2509106083"
loginstatus = False
logintry = 0
print("Selamat datang di halaman login")
while loginstatus == False:
    usn = str(input("Username\t:"))
    pw = str(input("Password\t:"))
    if(usn == nama and pw == nim):
        print(f"Login berhasil, selamat datang di Toko Infordeh {nama}")
        loginstatus = True
    elif(usn != nama and pw != nim):
        print("Username dan Password tidak valid")
        logintry += 1
    elif(usn != nama):
        print("Username tidak di temukan")
        logintry += 1
    else:
        print("Password salah")
        logintry += 1
    if(logintry < 3 and loginstatus != True):
        print("Silahkan coba lagi")
    elif(logintry == 3):
        print("Login gagal setelah 3 kali percobaan")
        break


    
total = 0
while loginstatus == True:
    harga = 0
    print("""
opsi 1 -> Sofa dengan Harga per unit Rp 500.000
opsi 2 -> Meja Belajar dengan Harga per unit Rp.250.000
opsi 3 -> Rak lemari dengan Harga per unit Rp.150.000
opsi 4 -> Keluar dari program
          """)
    opsi = int(input("Pilih opsi\t:"))
    if opsi == 1:
        print("Sofa")
        unit = int(input("Jumlah unit\t:"))
        for i in range(unit):
            harga += 500000
        total += harga
        print(f"Total unit sofa {unit} dengan harga Rp{harga}")
    elif opsi == 2:
        print("Meja Belajar")
        unit = int(input("Jumlah unit\t:"))
        for i in range(unit):
            harga += 250000
        total += harga
        print(f"Total unit meja belajar {unit} dengan harga Rp{harga}")
    elif opsi == 3:
        print("Rak Lemari")
        unit = int(input("Jumlah unit\t:"))
        for i in range(unit):
            harga += 150000
        total += harga
        print(f"Total unit rak lemari {unit} dengan harga Rp{harga}")
    elif opsi == 4:
        print("===== STRUK PEMBELIAN TOKO INFORDEH =====")
        print(f"Total harga awal\t\t: Rp{total}")
        if total == 0:
            break
        elif total >= 700000:
            total = total - (total*0.2)
            print("Bonus\t\t\t\t: Diskon 20%")
        elif total >= 500000 and total < 700000:
            total = total - (total*0.08)
            print("Bonus\t\t\t\t: Diskon 8%")
        elif total >= 150000 and total < 500000:
            total = total
            print("Bonus\t\t\t\t: Kitchen set")
        else:
            total = total
            print("Bonus\t\t\t\t: Tidak ada")
        print(f"Total bayar setelah bonus\t: Rp{total}")
        break

    else:
        print("Pilihlah opsi 1/2/3/4")

# Jika total bayar >= Rp.700.000, maka ia mendapat potongan 20% dari total bayar akhir.
# Jika total bayar >= Rp.500.000 dan total bayar < Rp.700.000, maka ia mendapat potongan 8% dari total bayar akhir.
# Jika total bayar >= Rp.150.000 dan < Rp.500.000, maka ia mendapat Kitchen Set.
