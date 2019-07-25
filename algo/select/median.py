from typing import List, Any

def medians_of_medians(array: List[Any], k: int):
    print(k)
    if (len(array)<= 5):
        return sorted(array)[k]
    else:
        medians = []
        for i in range(0, len(array), 5):
            j = i+5 if i+5 <= len(array) else len(array)
            medians.append(medians_of_medians(array[i:j], (j-i)//2))
        pivot = medians_of_medians(medians, len(medians)//2)

        low = [elem for elem in array if elem < pivot]
        high = [elem for elem in array if elem > pivot]

        index = len(low)

        if k < index:
            return medians_of_medians(low, k)
        elif k > index:
            return medians_of_medians(high, k-index-1)
        else:
            return pivot


"""
###Test###  
if __name__ == "__main__":
    import random
    arr = [random.randint(0,100) for i in range(10)]
    print(arr)
    k = 3
    elem = medians_of_medians(arr, k)
    arr.sort()
    print(k,elem, arr)
"""