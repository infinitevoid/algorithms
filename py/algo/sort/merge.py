from typing import List,Any

def merge_sort(array: List[Any], left: int, right: int) -> List[Any]:
    if(right-left <= 1): return array[left:right]
    middle = (right+left)//2
    a = merge_sort(array, left, middle)
    b = merge_sort(array, middle, right)
    return merge(a,b)

def merge(a: List[Any], b: List[Any]):
    i,j = 0,0
    new = []
    while i < len(a) and j < len(b):
        top_a, top_b = a[i], b[j]
        if top_a <= top_b:
            new.append(a[i])
            i += 1
        else:
            new.append(b[j])
            j += 1
    if i < len(a):
        new.extend(a[i:])
    elif j < len(b):
        new.extend(b[j:])
    return new

"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    print(merge_sort(arr, 0, len(arr)))
"""