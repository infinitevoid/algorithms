from typing import List, Any

def down_to(value, limit):
    for i in range(value, limit-1, -1): yield i 

def bubble_sort(array: List[Any], start = 0):
    if start == len(array)-1: return
    for i in down_to(len(array)-2, start):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
    bubble_sort(array, start+1)

"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    bubble_sort(arr)
    print(arr)
"""