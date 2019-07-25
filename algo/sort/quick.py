from typing import List,Any

def quick_sort(array: List[Any], left: int, right: int):
    if right-left <= 1: return
    index = partition(array, left, right)
    quick_sort(array, left, index)
    quick_sort(array, index, right)

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
    quick_sort(arr, 0, len(arr))
    print(arr)
"""