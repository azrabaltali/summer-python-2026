#yorum satırı 
#---variables---

name = "azra"
surname = "baltalı"
age = 23
student = True

print(name)
print(surname)
print(age)
print(student)

print(type(name))
print(type(surname))
print(type(age))
print(type(student))


#---list---
fruits = ["apple","banana","orange","strawberry"]
print(fruits)

fruits.append("kiwi")
print(fruits)

print(f"last fruit: {fruits[-1]}")

fruits.remove(fruits[0])
print(fruits)


#---dict---
ogrenci = {
    "isim": "azra",
    "soyisim": "baltalı",
    "bolum": "compeng",
    "yas" : 22
}

ogrenci["sehir"] = "adana"
print(ogrenci)

ogrenci["yas"] = 23
print(f"Yaş güncellendi : {ogrenci}")

# Tüm anahtarları (keys) göster
print(f"Anahtarlar: {ogrenci.keys()}")

# Tüm değerleri (values) göster
print(f"Değerler: {ogrenci.values()}")


#---tuples---- listeye çok benzer ama tek farkı değiştirilemez!! append ve remove kullanamazsın
# Haftanın günleri (asla değişmez!)
gunler = ("Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma")
print(gunler)


#----f-string formatı -----
urun = "laptop"
fiyat = 15000
adet = 3

# Temel kullanım
print(f"Ürün: {urun}, Fiyat: {fiyat} TL")

# İçinde işlem yapma
print(f"{adet} adet {urun} toplam: {fiyat * adet} TL")

# Sayı formatlama (virgüllü)
sayi = 3.14159265
print(f"Pi sayısı: {sayi:.2f}")  # 2 basamak: 3.14

# Hizalama
print(f"{'Ürün':<10} {'Fiyat':<10}")
print(f"{urun:<10} {fiyat:<10} TL")