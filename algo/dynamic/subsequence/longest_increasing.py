from typing import List, Any

"""
O(n*log n) algorithm: line 19
O(n^2) algorithm: line 39
"""


def binary_search(array: List[Any], key: Any, left: int, right: int):
    while right-left > 1:
        m = (right+left) // 2
        if array[m] > key:
            right = m  
        else:
            left = m
    return right

def longest_increasing_subsequence(array: List[Any]):
    tail_array    = [0 for i in range(len(array))]
    tail_array[0] = array[0]
    length = 1
    for elem in array[1:]:
        if elem < tail_array[0]:
            tail_array[0] = elem
        elif elem > tail_array[length-1]:
            tail_array[length] = elem
            length += 1
        else:
            tail_array[binary_search(array, elem, 1, length-1)] = elem
    return length

"""
###Test###
if __name__ == "__main__":
    A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ] 
    print(longest_increasing_subsequence(A))
"""

def dynamic_lis(array: List[Any]):
    dp = [1 for i in range(len(array))]
    for i, x in enumerate(array):
        for j in range(0,i):
            y = array[j]
            if x > y:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[len(array)-1]

"""
###Test###
if __name__ == "__main__":
    arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
    print(dynamic_lis(arr)) 
"""
    
