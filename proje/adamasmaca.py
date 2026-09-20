import random

with open("words.txt", "r", encoding="utf-8") as dosya:
    kelimeler = dosya.readlines()

kelimeler = [satir.strip().lower() for satir in kelimeler]

secilen_kelime = random.choice(kelimeler)

gizli_kelime = ""
for harf in secilen_kelime:
    if harf == " ":
        gizli_kelime += " "
    else:
        gizli_kelime += "_"

kalan_hak = 6
tahmin_edilenler = []

print("Seçilen kelime: ", secilen_kelime)   # test için, sonra sileceğiz
print("gizli hali: ", gizli_kelime)

# ============ ANA OYUN DÖNGÜSÜ ============
while True:
    # --- 1) geçerli bir harf al ---
    while True:
        tahmin = input("harf: ").lower()

        if tahmin == "":
            print("Boş giremezsin bir harf tahmin etmelisiniz.")
        elif len(tahmin) > 1:
            print("Tek harf girmelisiniz!")
        elif not tahmin.isalpha():
            print("Sadece harf girebilirsiniz!")
        elif tahmin in tahmin_edilenler:
            print(f"'{tahmin}' harfini zaten tahmin ettiniz!")
        else:
            break

    # --- 2) tahmini listeye ekle ---
    tahmin_edilenler.append(tahmin)

    # --- 3) harf kelimede var mı? ---
    if tahmin in secilen_kelime:
        print(f"'{tahmin}' kelimede var ✅")

        yeni_gizli = ""
        for i in range(len(secilen_kelime)):
            if secilen_kelime[i] == tahmin:
                yeni_gizli += tahmin
            else:
                yeni_gizli += gizli_kelime[i]
        gizli_kelime = yeni_gizli
    else:
        print(f"'{tahmin}' kelimede yok ❌")
        kalan_hak -= 1

    # --- 4) durumu göster ---
    print("gizli hali: ", gizli_kelime)
    print("kalan hak: ", kalan_hak)

    # --- 5) kazandı mı? ---
    if "_" not in gizli_kelime:
        print(f"🎉 KAZANDIN! Kelime: {secilen_kelime}")
        break

    # --- 6) kaybetti mi? ---
    if kalan_hak == 0:
        print(f"💀 KAYBETTİN! Kelime: {secilen_kelime}")
        break