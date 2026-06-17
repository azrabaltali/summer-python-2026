def reverse_stack(name):
    stack = []
    n = len(name)
    reverse_name = ""
    for i in range(n):  
        stack.append(name[i])
        print(stack)
    for j in range(len(stack)):
        reverse_name = reverse_name + stack.pop()
        print(stack)

    return reverse_name

isim = "azra"
print(f"name reverse:{reverse_stack(isim)}")

# Python'un slicing'i ile (Stack kullanmadan)
def reverse_string_simple(s):
    return s[::-1]

isim = "baltalı"
print(f"name reverse:{reverse_string_simple(isim)}")

def sayilari_ters_cevir(sayilar):
    stack = []
    sonuc = []
    
    # Bu kısmı while ile yaz
    for sayi in sayilar:
        stack.append(sayi)
    
    while stack:
        sonuc.append(stack.pop())
    
    return sonuc

# Test
print(sayilari_ters_cevir([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]