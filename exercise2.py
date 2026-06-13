# 1. Yaş kontrolü (if-else)
age = int(input("age:"))
if age >= 18:
    print("Oy kullanabilirsin.")
else:
    print("Oy kullanamazsın!")
# Kullanıcıdan yaşını al, 18 ve üzerindeyse "Oy kullanabilirsin"
# değilse "Oy kullanamazsın" yazdır.



# 2. 1'den 20'ye kadar olan sayıları ekrana yazdır (for döngüsü ile)
for num in range(1,20):
    print(num)


# 3. Liste dolaşma (for)
# "markalar = ["Apple", "Samsung", "Xiaomi", "Huawei"]" listesindeki
list = ["Apple", "Samsung", "Xiaomi", "Huawei"]
for brand in list:
    print(f"Marka: {brand}")
# her markayı "Marka: ..." şeklinde yazdır.



# 4. while döngüsü
# 1'den başlayarak 10'a kadar olan sayıları yazdıran while döngüsü yaz.
i = 1
while i<10:
    print(i)
    i += 1



# 5. break kullanımı (ZOR)
# 1'den başlayarak sayıları toplayan, toplam 50'yi geçtiğinde döngüyü durduran program yaz.
total = 0
number = 1 
while True: #sonsuz döngü başlatıyoruz çünkü bazen döngünün ne zaman biteceğine karar veremeyiz ve buna döngünün içinde karar veririz.
    total = total + number
    print(f"{number} eklendi, toplam: {total}")
    
    if total > 50:
        print(f"toplam elliyi geçti. {total}")
        break
        
    number += 1