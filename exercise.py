# ----- ALIŞTIRMALAR -----

# 1. Değişkenler
# Kendi adını, yaşını ve yaşadığın şehri değişkenlere tanımla ve f-string ile yazdır.
name = "Azra"
surname = "Baltalı"
age = 23
city = "Adana"
print(f"Ben {name} {surname}, {age} yaşındayım {city}'da yaşıyorum.")
# Kodunu buraya yaz:


# 2. Listeler
list = ["red", "green", "blue"]
list.append("orange")  
# 3 farklı renkten oluşan bir liste oluştur. Listenin sonuna yeni bir renk ekle.
print(f"ikinci renk: {list[1]}")
# Sonra ikinci rengi ekrana yazdır.


# 3. Sözlükler
book = {
    "isim" : "İstanbul Hatırası",
    "yazar" : "Ahmet Ümit",
    "page" : 673
}
# Bir kitabın bilgilerini içeren bir sözlük oluştur (başlık, yazar, sayfa sayısı).
# Sözlükten sadece başlığı yazdır.
print(f"kitabın ismi: {book['isim']}")



# 4. Tuple
week = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
# Haftanın 5 gününü bir tuple içinde tanımla. 3. günü (Çarşamba) ekrana yazdır.
print(f"haftanın üçüncü günü: {week[2]}")


# 5. Tamamlama (ZOR)
# Bir öğrenci sözlüğü oluştur: (isim, notlar_listesi)
ogrenci = {
    "ad" : "Ahmet",
    "soyad" : "Baltalı",
    "mat" : 90 ,
    "english" : 100
}

print(f"avg: {(ogrenci['mat']+ogrenci['english'])/2}")
# Öğrencinin not ortalamasını hesaplayıp yazdır.
