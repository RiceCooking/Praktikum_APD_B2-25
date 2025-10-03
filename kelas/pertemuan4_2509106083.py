for a in range(10 , 0, -1):
    print(a)

data = ((250, "A"), (251, "B"))
for x, y in data:
    print(x ,y)

for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")