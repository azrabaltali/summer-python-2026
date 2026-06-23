# Barınak listesi: (tür, isim)
barinak = []

def ekle(tur, isim):
    barinak.append([tur, isim])  # Liste olarak sakla
    print(f"✅ {isim} ({tur}) eklendi")

def goster():
    if not barinak:
        print("📋 Barınak boş")
        return
    print("\n📋 Barınak:")
    for i, hayvan in enumerate(barinak):
        print(f"  {i+1}. {hayvan[1]} ({hayvan[0]})")

def sahiplendir():
    if not barinak:
        print("❌ Boş")
        return
    hayvan = barinak.pop(0)
    print(f"🏠 {hayvan[1]} ({hayvan[0]})")

def kopek_sahiplendir():
    for i, hayvan in enumerate(barinak):
        if hayvan[0] == "köpek":
            sahiplenilen = barinak.pop(i)
            print(f"🏠 {sahiplenilen[1]} (köpek)")
            return
    print("❌ Köpek yok")

def kedi_sahiplendir():
    for i, hayvan in enumerate(barinak):
        if hayvan[0] == "kedi":
            sahiplenilen = barinak.pop(i)
            print(f"🏠 {sahiplenilen[1]} (kedi)")
            return
    print("❌ Kedi yok")

# Test
print("=" * 40)
ekle("köpek", "Karabaş")
ekle("kedi", "Pamuk")
ekle("köpek", "Boncuk")
ekle("kedi", "Minnoş")
ekle("köpek", "Zeytin")

goster()

print("\n" + "=" * 40)
sahiplendir()
kopek_sahiplendir()
kedi_sahiplendir()

goster()