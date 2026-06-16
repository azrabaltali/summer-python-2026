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