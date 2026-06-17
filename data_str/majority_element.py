def majority_element_dict(nums):
    counts = {}
    n = len(nums)
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > n // 2:
            return num
    return None

# Test
print(majority_element_dict([3, 2, 3]))          # 3
print(majority_element_dict([2, 2, 1, 1, 1, 2, 2]))  # 2

def majority_element_sort(nums):
    nums.sort()
    return nums[len(nums) // 2]

# Test
print(majority_element_sort([3, 2, 3]))           # 3
print(majority_element_sort([2, 2, 1, 1, 1, 2, 2])) # 2

def majority_element_voting(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
        print(f"Sayı: {num}, Aday: {candidate}, Sayaç: {count}")
    
    return candidate

# Test
print("\nSonuç:", majority_element_voting([2, 2, 1, 1, 1, 2, 2]))