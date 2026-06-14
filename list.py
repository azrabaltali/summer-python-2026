square_list = []
for i in range(1,11):
    square_list.append(i**2)

print(square_list)

# or 

square2 = [i ** 2 for i in range(1,11)]
print(f"options2:\n{square2}")

names = ["azra","baltalı","ahmet","muhsin"]
big_char = [name.upper() for name in names]
print(big_char)


numbers = range(1,11)
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

namess = ["azra","baltalı","ahmet","muhsin"]
long_namess = [name for name in namess if len(name)>4]
print(f"long names:{long_namess}")
print(f"all names:{namess}")


cube = [a ** 3 for a in range(1,21)]
print(f"cube:{cube}")

third = range(1,51)
div_third = [div for div in third if div % 3 == 0]
print(f"division third ok:{div_third}")

isims = ["azra","baltalı","ahmet","muhsin"]
hi = [f"merhaba {isim}" for isim in isims]
print(hi)


ip_address = ["10.0.0.1", "192.168.1.10", "192.168.1.15", "172.16.0.1", "192.168.1.20", "8.8.8.8"]
special_ip = [ip for ip in ip_address if ip.startswith("192.168.1")]
print(special_ip)

