from typing import List, Any

def binary_search(sorted_array: List[Any], element: Any, left: int, right: int) -> int:
    if (right == left):
        return -1
    middle = (right+left)//2
    if element > sorted_array[middle]:
        return binary_search(sorted_array, element, middle, right)
    elif element < sorted_array[middle]:
        return binary_search(sorted_array, element, left, middle)
    else: #element == sorted_array[middle]
        return middle


"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    test = arr[0]
    arr.sort()
    print(binary_search(arr,test,0,len(arr)),test,arr)

"""