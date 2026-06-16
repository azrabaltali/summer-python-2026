def palindrome(palind):
    n = len(palind)
    for i in range(n // 2):  # sadece yarısına kadar kontrol et
        j = n - 1 - i        # j sondan gelen indeks
        if palind[i] != palind[j]:
            return False     # bir eşleşmezse False
    return True              # tüm eşleşmeler doğruysa True

# Test
print(palindrome("kayak"))   # True
print(palindrome("hello"))   # False
print(palindrome("aba"))     # True
print(palindrome("abca"))    # False


#remove duplicates:
def remove_duplicates_set(s):
    seen = set()
    result = ""
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    
    return result

# Test
print(remove_duplicates_set("programlama"))  # "progaml"
print(remove_duplicates_set("hello"))        # "helo"
print(remove_duplicates_set("banana"))       # "ban"