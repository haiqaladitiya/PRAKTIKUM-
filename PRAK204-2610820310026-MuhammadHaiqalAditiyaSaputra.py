angka = []

inputan = input().split()

angka.extend(inputan)

while(len(angka) < 2):
    inputan = input().split()
    angka.extend(inputan)

jari_jari = float(angka[0])
tinggi = float(angka[1])

Volume = 22.0 / 7.0 * jari_jari * jari_jari * tinggi
Luas = 2 * 22.0 / 7.0 * jari_jari * (jari_jari + tinggi)
Keliling = 2 * 22.0 / 7.0 * jari_jari

print(" ")
print(f"Volume   = {Volume:.2f}")
print(f"Luas     = {Luas:.2f}")
print(f"Keliling = {Keliling:.2f}\n")
