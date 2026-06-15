import math # import modül_name (tüm modülü içeri aktarır)

#from modül_name import function (sadece ihtiyacımız olan)
from datetime import datetime

#import modül_name as kıslaltma mesela
import random as rnd #(takma ad)


# random -> rastgele sayılar
import random

rand_number = random.randint(1,100)
print(f"random number: {rand_number}")

fruits = ["apple", "banana", "watermelon"]
rand_fruits = random.choice(fruits)
print(f"random fruits: {rand_fruits}")

#---------------------------------------
#dosya okuma 
#dosyaya yazma (w = write)
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("ım learning python\n")
    file.write("ı learn file operation today.\n")
    file.write("it is a different topic.\n")

print("notes.txt created and write.")

#file read (r = read)
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"file content:\n{content}")

#append (a = append)
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("adding new line\n")
    file.write("intern")

print("new lines were added to file")

with open("notes.txt", "r", encoding="utf-8") as file:
    print("new content:")
    for row in file:
        print({row.strip()})
