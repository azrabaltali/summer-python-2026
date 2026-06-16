#An array is a data structure that has a fixed size and is indexable. It can store elements of the same data types.
#Array indexing start from 0 and we can access each element by using its index.
#Fast access: Each element has a index so we can directly access any element in constant time O(1)
#cache-friendly: Array elements are store in contiguous memory locations.
#Fixed-size: The size of an array is fixed after it is created. If we need more space, we usually have to create a new array and copy the elements.
#expensive insertion and deletion O(n): Insertion and deletion in the middle of an array because other elements must be shifted to maintain the order.

def again_elements(arr):
    seen = set()
    for element in arr:
        if element in seen:
            return element
        seen.add(element)

    return None

print(f"tekrar eden eleman: {again_elements([1,2,2,2,3,3,4,5,6])}")

def reverse(array):
    n = len(array)
    for i in range(n//2):
        j = n - 1 - i
        array[i] , array[j] = array[j], array[i]
    return array

my_list = [1,2,3,4,5,6]
print(f"mylist reverse: {reverse(my_list)}") 
            

#max subarray
def max_sub_array(arr2):
    now_best = 0
    total_best = 0

    for i in range(len(arr2)):
        now_best = now_best + arr2[i]
        if now_best < 0:
            now_best = 0
            print("negative.")
        else:
            if now_best > total_best:
                total_best = now_best
    return total_best

my_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"my max sub array:{max_sub_array(my_array)}")