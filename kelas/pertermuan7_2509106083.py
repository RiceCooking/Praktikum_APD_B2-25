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
        print(f"Faktorial dari {bil}\t:{faktorial(bil)}")
        break
    except ValueError:
        print("Input hanya berupa angka")
        continue