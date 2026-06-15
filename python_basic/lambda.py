#nameless mini function
def square(x):
    return x ** 2

print(f"def func: {square(5)}")

square_lambda = lambda x: x**2
print(f"lambda func: {square_lambda(5)}") 

add = lambda a, b: a + b
print(f"add: {add(5,3)}")


max_number = lambda a,b: a if a > b else b
print(f"max number:{max_number(8,17)}")

#sorted()
students = [
    {"isim":"Ahmet", "note":85},
    {"isim":"Muhsin", "note":65},
    {"isim":"Azra", "note":95},
    {"isim":"Emre", "note":88}
]

print("original list:")
for o in students:
    print(f"{o['isim']:{o['note']}}")

#nota göre sıralayalım:
nota_gore = sorted(students, key=lambda x: x['note'])
print("nota göre sıralı")
for o in nota_gore:
    print(f"{o['isim']}: {o['note']}")

#map listedeki her elemana işlem yapar:
isimler = ["ali", "ayşe", "mehmet"]
buyuk_harfler = list(map(lambda isim: isim.upper(), isimler))
print(f"\nOrijinal isimler: {isimler}")
print(f"Büyük harfler (map): {buyuk_harfler}")
