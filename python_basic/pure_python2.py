# break: döngüyü tamamen durdur
print("break örneği (5'te dur):")
for i in range(1, 11):
    if i == 5:
        print("Döngü durduruldu!")
        break
    print(i)

# continue: sadece o adımı atla
print("\ncontinue örneği (çift sayıları atla):")
for i in range(1, 11):
    if i % 2 == 0:  # çift sayı mı?
        print(f"{i} atlandı")
        continue
    print(f"Tek sayı: {i}")