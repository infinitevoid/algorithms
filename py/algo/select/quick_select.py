from typing import List, Any

def quick_select(array: List[Any], k: int, left: int, right: int):
    if k == 0:
        minimum = array[left]
        for i in range(left, right):
            if array[i] < minimum: minimum = array[i]
        return minimum
    
    index = partition(array, left, right)
    if index > k:
        return quick_select(array, k, left, index)
    else:
        return quick_select(array, k-index, index, right)
    
def partition(array: List[Any], left: int, right: int) -> int:
    pivot = array[right-1]
    i = left-1
    for j in range(left,right):
        if array[j] <= pivot:
            i +=1
            array[i],array[j] = array[j],array[i]
    return i

"""
###Test###  
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    k = 5
    elem = quick_select(arr, k, 0, len(arr))
    arr.sort()
    print(k,elem, arr)
"""