# mobil = ["Toyota", "Honda", "Ferrari", "BMW"]
# print(mobil[:2])#[start : stop : step]
# print(mobil[:1:-1])#step:-1 dari belakang. index di mobil 3..
# del mobil[1]
# print(mobil)# honda hilanh kareana di inddex ke 1 = "honda"
animal = ["Kucing", "Anjing", "Kelinci", "Hamster", ["Penyu", "Kura-Kura"]]
animal[4].insert(0, "Hiu")#di index ke 4 pada animal di tambahkan hiu ke index 0 dan index yang awalnya 0 dan 1 -> 1 dan 2 karena hiu jadi yang pertama
print(animal)
print(len(animal))