#Materi Set & Dictionary
# print("SET\n")
# data = {"Andi", 4, "Seven"}#ga beruratan
# print(data)

# for i in data:
#     print(i)

# prima = {2, 3, 5, 7}
# print("Ini aslinya")
# for i in prima:
#     print(i)

# prima.add(11)
# print("\nNambahin element pakai add()")
# for i in prima:
#     print(i)

# prima.discard(3)
# print(f"Hapus pakai discard\n{prima}")

#Dictionary

# kalkulus : dict = { # var : dict = {keys, values} -> {keys, values} = items
#     "Limit" : 100,
#     "Turunan" : 101,
#     "Intergral" : 1000,
# }

# print(f"Ini ambil intergral -> {kalkulus[f"Intergral"]}")# aksesnya harus pakai  keys
# print(f"Ini pakai var:dict.keys() {kalkulus.keys()}")

Biodata = { 
"Nama" : "Ananda Daffa Harahap", 
"NIM" : 2409106050, 
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Algoritma"], 
"Mahasiswa_Aktif" : True, 
"Social Media" : {  "Instagram" : "daffahrhap"  }

}
print("\nIni akses Pakai Style dict[keys][values:list(index)] KRS index ke 1")
print(Biodata["KRS"][1])
print("\nIni akses Pakai dict.get() KRS index ke 1")
print(Biodata.get("KRS")[1])
print(Biodata.get("Social Media")["Instagram"])
