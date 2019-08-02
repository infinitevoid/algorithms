from typing import List, Any
import heap

def selection_sort(array: List[Any]):
    for i in range(0,len(array)):
        _min,j = array[i],i
        for k in range(j,len(array)):
            if array[k] < _min: _min, j = array[k], k
        array[i],array[j] = array[j],array[i]

def flash_sort(array: List[Any], buckets: int = 10):
    if len(array) <= 16:
        selection_sort(array)
        return
    _min,_max = array[0],array[0]
    for elem in array:
        _min = min(elem, _min)
        _max = max(elem, _max)
    step = (_max - _min)/(buckets-1)
    if step == 0: return
    bs = [[] for i in range(buckets)]
    for elem in array:
        ind = int((elem - _min)/step)
        bs[ind].append(elem)
    i = 0
    for arr in bs:
        flash_sort(arr, buckets)
        for elem in arr:
            array[i] = elem
            i += 1
    bs.clear()
    del bs

if __name__ == "__main__":
    import random
    arr = [random.randint(-1000,1000) for i in range(100)]
    flash_sort(arr)
    print(arr)