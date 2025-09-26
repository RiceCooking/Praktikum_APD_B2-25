# angka = 2
# if angka > 5:
#     print("Angka lebih besar dari 5")


a = [5, 6]
print(sum(a))
print("\n Masukkan angka")
x = int(input())
a = ""
if(x < 0 or x > 5):
    a += "Error"
    print(a)
if(x >= 0 and x <= 5):
   a += "Berhasil"
   print(a)
if(x == 6):
    a += "Enam"
    print(a)


