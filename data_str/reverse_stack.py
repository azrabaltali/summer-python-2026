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