import random

with open("words.txt","r", encoding="utf-8") as dosya:  #with kullanmazsak dosyayı elle kapatmamız gerekir.
    kelimeler = dosya.readlines() #readlines her satırı ayrı bir eleman olarak listeye koyar

kelimeler = [satir.strip().lower() for satir in kelimeler]

    #strip() baş ve sondaki boşlukları temizler. 
    #lower() hepsini  küçük harfe çevirir.

secilen_kelime = random.choice(kelimeler)

gizli_kelime = ""
for harf in secilen_kelime:
    if harf == " ":
        gizli_kelime += " "
    else:
        gizli_kelime += "_"

kalan_hak = 6
tahmin_edilenler = [] #oyuncunun şimdiye kadar kullandığı harfler

print("Seçilen kelime: ", secilen_kelime)
print("gizli hali: ", gizli_kelime)
print("kalan hak: ", kalan_hak)