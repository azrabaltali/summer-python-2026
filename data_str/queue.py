# FIFO First In First Out

# Enqueue (kuyruğa ekle)
# Dequeue (kuyruktan çıkar)

queue = []

queue.append(10)
print(queue)

queue.append(20)
queue.append(50)

print(queue)

first_element = queue.pop(0)
print(first_element)

front = queue[0]
print(front)

if len(queue) == 0:
    print("Queue is empty!")


def bank():
    kuyruk = []
    musteri_no = 1

    while True:
        print("\n--- Banka Sırası ---")
        print(f"Müşteri sayısı: {len(kuyruk)}")
        print("Kuyruk:", kuyruk)
        print("1. Yeni müşteri ekle")
        print("2. Müşteri çağır")
        print("3. Çıkış")

        secim = input("Seçiminiz:")
        
        if secim == "1" :
            kuyruk.append(musteri_no)
            print(f"{musteri_no} nolu müşteri eklendi.")
            musteri_no += 1

        elif secim == "2":
            if kuyruk:
                musteri = kuyruk.pop(0)
                print(f"{musteri} nolu müşteri çağrıldı.")
            else:
                print("Sırada müşteri yok")
                input("Devam etmek için Enter'a basın...")
        elif secim == "3":
            print("Have a nice day!")
            break

bank()
            
