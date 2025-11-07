import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



x = [1, 2, 3, 4, 5]
y = [10, 35, 20, 70, 60]
y2 = [12, 43, 56, 23, 67]
plt.figure(figsize=(8, 4))
# plt.plot() untuk masing-masing garis
plt.plot(x, y, marker="o", color="blue", label="Matematika")
plt.plot(x, y2, color="red", marker="h", linestyle="--", label="Fisika")
# Detail elemen untuk memambahkan teks
plt.title("Contoh Grafik")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")
plt.grid(True)
# Nambahin keterangan, tapi jangan lupa tambahkan label
plt.legend()
plt.show()
plt.savefig("Real Penggunaan") #Menyimpan Gambar