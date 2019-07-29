from typing import List, Any

def interpolation_search_rec(array: List[Any], key: Any, left: int, right: int) -> int:
    low = array[left]
    high = array[right-1]
    if low == high or key < low or key > high:
        return -1
    ind = left + int((key - low) * (right-1-left)/(high-low))
    if key < array[ind]:
        return interpolation_search_rec(array, key, left, ind)
    elif key > array[ind]:
        return interpolation_search_rec(array, key, ind+1, right)
    else:
        return ind

def interpolation_search(array: List[Any], key: Any) -> int:
    left = 0
    right = len(array)-1
    low, high = array[left], array[right]
    
    while low != high and low < key and key < high:
        ind = left + int((key-low)*(right-left)/(high-low))
        if key > array[ind]:
            left = ind + 1
            low  = array[left]
        elif key < array[ind]:
            right = ind - 1
            high  = array[right]
        else:
            return ind
    if low == key:
        return left
    return -1

"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    test = arr[0]
    arr.sort()
    print(interpolation_search(arr, test))
    print(interpolation_search_rec(arr,test,0,len(arr)))
    print(test,arr)
"""