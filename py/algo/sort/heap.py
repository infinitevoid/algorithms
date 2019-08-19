from typing import List, Any

def down_to(value, limit):
    for i in range(value, limit-1, -1): yield i 

def heap_sort(array: List[Any]):
    for i in down_to(len(array)//2 - 1, 0):
        heapify(array, len(array), i)
    for j in down_to(len(array)-1, 0):
        array[j], array[0] = array[0], array[j]
        heapify(array, j, 0)


def heapify(array: List[Any], length: int, start: int):
    largest = start
    left  = 2 * start + 1
    right = 2 * start + 2
    if left < length and array[largest] < array[left]:
        largest = left
    if right < length and array[largest] < array[right]:
        largest = right
    if largest != start:
        array[start], array[largest] = array[largest], array[start]
        heapify(array, length, largest)

"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    heap_sort(arr)
    print(arr)
"""