# angka = 2
# if angka > 5:
#     print("Angka lebih besar dari 5")
a = [5, 6]
print(sum(a))
print("\n Masukkan angka")
x = int(input())
a = ""
if(x < 0 or x > 5):
    if(x == 6):
            a = a.replace("Error", "")
            print(a)
    else:
        a += "Error"
        print(a)
if(x >= 0 and x <= 5):
   a += "Berhasil"
   print(a)
if(x == 6):
    a += "Enam"
    print(a)

# Bentuk awal
nilai = 70
if nilai >= 60:
    status = "Lulus"
else:
    status = "Tidak Lulus"
print(status)
# output
# Lulus
# Menggunakan Ternary Operator
nilai = 70
status = "Lulus" if nilai >= 60 else "Tidak Lulus"
print(status)
# output
# Lulus
