from typing import List, Any
from heapq import heapify, heappop

def kth_smallest(array: List[Any], k: int):
    copy = array[:]
    heapify(copy)
    for i in range(k): heappop(copy)
    return heappop(copy)

###Test###
if __name__ == "__main__":
    arr = [2,22,5,7,2,65,545,54,3,23,43]
    k = 3 
    print(kth_smallest(arr,k))
    arr.sort()
    print(k, arr)
