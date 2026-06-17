# LIFO : Last in First out
# en son kim aramışsa önce onun çağrısına dönersin,
# tabaklarda en son koyduğun tabağı geri alırsın.
# push(x) add element insert a new element into the stack
# pop() remove the top element from the stack removes and returns the top element 
# peek() view the top element without removing it returns the top element
# is_empty() return True or False
# size() get the number of elements in the stack 


def temperature(arr):
    day = []
    n = len(arr)
    for i in range(n):
        found = False
        for j in range(i+1,n):
            if arr[i] < arr[j]:
                day.append(j-i)
                found = True
                break #ilk bulduğunda dur
        if not found:
            day.append(0) #hiç bulamadıysa
        
    return day


hot = [73, 74, 75, 71, 69, 72, 76, 73]
print(f"hotter days: {temperature(hot)}")
            

#stackli değil arrayli bir çözüm ve bunu henüz githuba pushlamadım... 
        
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []  # İndeksleri tutar
    
    for i in range(n):
        # 1. Stack'teki daha soğuk günleri kontrol et
        while stack and temps[stack[-1]] < temps[i]:
            # 2. O günü stack'ten çıkar
            prev = stack.pop()
            # 3. Kaç gün sonra olduğunu hesapla
            result[prev] = i - prev
        
        # 4. Bugünü stack'e ekle (ileride hatırlamak için)
        stack.append(i)
    
    return result

hot = [73, 74, 75, 71, 69, 72, 76, 73]
print(f"hotter days: {daily_temperatures(hot)}")