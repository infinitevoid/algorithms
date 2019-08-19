from typing import List,Any

def selection_sort(array: List[Any], start = 0):
    if start >= len(array): return
    index, minimum = start, array[start]
    for i in range(start+1, len(array)):
        if array[i] < minimum:
            minimum, index = array[i], i
    array[start], array[index] = array[index], array[start]
    selection_sort(array, start+1)

"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    selection_sort(arr)
    print(arr)
"""