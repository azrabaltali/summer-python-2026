import datetime

def diaries_write():
    text = input("Mesajınızı girin: ")
    
    # Şu anki tarih ve saati al
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # "a" ile dosyaya EKLE (öncekiler silinmez)
    with open("message.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {text}\n")
    
    print("Günlüğe kaydedildi!\n")

def diaries_read():
    try:
        with open("message.txt", "r", encoding="utf-8") as file:
            contents = file.read()
            print("\n--- GÜNLÜK İÇERİĞİ ---")
            print(contents)
            print("------------------------\n")
    except FileNotFoundError:
        print("Henüz hiç günlük girişi yok. Önce yazı ekleyin!\n")

# Ana program
while True:
    print("\n--- DİARIES APPLICATION ---")
    print("1. Write to diary")
    print("2. Read the diary")
    print("3. Logout")

    choice = input("Seçiminiz: ")

    if choice == "1":
        diaries_write()  
    elif choice == "2":
        diaries_read()   
    elif choice == "3":
        print("Good Bye!")
        break
    else:
        print("Invalid choice!")