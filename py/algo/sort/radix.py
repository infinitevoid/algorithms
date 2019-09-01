from typing import List

# lsd radix sort for 32bit ints
def lsd_radix_sort(array: List[int]):
    count = [0 for i in range(256)]
    offset = [0 for i in range(256)]
    buffer = array[:]
    for rep in range(4):
        for elem in array:
            key = (elem >> (rep*8)) & 255
            count[key] += 1

        offset[0] = 0
        for i in range(1,256):
            offset[i] = offset[i-1] + count[i-1]
            count[i-1] = 0 #clear on the fly
        count[255] = 0

        for elem in array:
            key = (elem >> (rep*8)) & 255
            j = offset[key]
            buffer[j] = elem
            offset[key] += 1

        for i in range(len(array)):
            array[i] = buffer[i]
    
"""
###Test###
if __name__ == "__main__":
    import random
    arr = [random.randint(0,123456) for i in range(10)]
    print("a:",arr)
    lsd_radix_sort(arr)
    print(arr)
"""