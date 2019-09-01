from typing import List, Any

def binary_search_rec(sorted_array: List[Any], element: Any, left: int, right: int) -> int:
    if (right == left):
        return -1
    middle = (right+left)//2
    if element > sorted_array[middle]:
        return binary_search_rec(sorted_array, element, middle, right)
    elif element < sorted_array[middle]:
        return binary_search_rec(sorted_array, element, left, middle)
    else: #element == sorted_array[middle]
        return middle

def binary_search(array: List[Any], key: Any):
    left, right = 0, len(array)
    while left != right:
        ind = (left+right)//2
        if key > array[ind]:
            left = ind + 1
        elif key < array[ind]:
            right = ind - 1
        else:
            return ind
    if array[left] == key:
        return left
    return -1
    
"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    test = arr[0]
    arr.sort()
    print(binary_search(arr,test))
    print(binary_search_rec(arr,test,0,len(arr)))
    print(test,arr)
"""