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

# Biodata = { 
# "Nama" : "Ananda Daffa Harahap", 
# "NIM" : 2409106050, 
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Algoritma"], 
# "Mahasiswa_Aktif" : True, 
# "Social Media" : {  "Instagram" : "daffahrhap"  }

# }
# print(Biodata["Nama"])
# print(Biodata.get("Nama"))
# print("\nIni akses Pakai Style dict[keys][values:list(index)] KRS index ke 1")
# print(Biodata["KRS"][1])
# print("\nIni akses Pakai dict.get() KRS index ke 1")
# print(Biodata.get("KRS")[1])
# print(Biodata.get("Social Media")["Instagram"])


# mahasiswa = {
#     83 :{
#         "Nama" : "Andi",
#         "Kelas" : "B",
#         "Hobi" : "Tidur"
#     },
#         80 :{
#         "Nama" : "Budi",
#         "Kelas" : "A",
#         "Hobi" : "Ngantuk"
#     },
# }

# for i, j in mahasiswa.items():
#     print(f"{i}")
#     for x,y in j.items():
#         print(x, y)
#     print("")
#Bagian Update
# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror" 
# } 
 
# #Sebelum Diubah 
# print(Film) 
# Film["Gen Z"] = "Action" 
# Film.update({"Naruto" : "Comedy"}) 
# Film.update({"The Conjuring" : "Tragedy"}) # kalo keys nya sudah ada otomatis ganti valuenya
# Film["Sherlock Holmes"] = "Action" 
# print(Film) 

data = { 
"Nama" : "Daffa", 
"Umur" : 19, 
"Jurusan" : "Informatika" 
} 
#Sebelum Dihapus 
print(data) 
 
del data["Nama"] 
#Setelah diubah 
print(data) 
 
#memanggil data yang telah dihapus 
print(data.get("Nama")) 


key = "apel", "jeruk", "mangga" 
 
value = 1 
 
buah = dict.fromkeys(key, value) 
 #{'apel': 1, 'jeruk': 1, 'mangga': 1} 
print(buah) 
 
