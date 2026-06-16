def two_add(arr):
    target = 9
    m = 0 
    for i in range(len(arr)):
        m = arr[i] + arr[i-1]  # burada i-1 kullanmak 0. indexte -1 e sebep oluyor bu da py de dizinin son elemanına tekabül ediyor.
        if m == target:
            print(f"targeta ulaşıldı!! {target}")
            return f"{arr[i]} and {arr[i-1]}"    #indexleri döndürecez değerleri değil bu da bir hata
    return None

nums = [2, 7, 11, 15]
print(f"target: {two_add(nums)}")

# düzenlenmiş fonksiyon:
def two_add_adjacent(arr, target): # targetı sabit olarak değil parametre olarak aldık.
    for i in range(len(arr) - 1):  # son elemana kadar değil
        m = arr[i] + arr[i+1]      # yan yana elemanlar
        if m == target:
            print(f"targeta ulaşıldı!! {target}")
            return [i, i+1]        # indeksleri döndür
    return None

nums = [2, 7, 11, 15]
print(two_add_adjacent(nums, 9))  # [0, 1]

#sadece yan yana olanları değil tüm çiftleri kontrol edelim şimdi de:
def two_sum_bruteforce(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test
nums = [2, 7, 11, 15]
target = 9
print(two_sum_bruteforce(nums, target))  # [0, 1]





