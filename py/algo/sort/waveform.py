from typing import List, Any

def swap(array: List[Any], i: int, j: int):
    array[i], array[j] = array[j], array[i]

def waveform(array: List[Any]):
    for i in range(0,len(array),2):
        if i > 0 and (array[i] < array[i-1]):
            swap(array, i-1, i)
        if i < len(array) - 1 and (array[i] < array[i+1]):
            swap(array, i+1, i)


"""
###Test###
if __name__ == "__main__":
    arr = [1,2,3,7,8,9,7,6,5,4,3]
    waveform(arr)
    print(arr)
"""