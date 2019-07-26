from typing import List, Any

def max_subarray(array: List[Any]):
    current_max, current_val = 0, 0

    curr_start, curr_end = 0,0
    max_start, max_end = 0, 0

    for i, elem in enumerate(array):
        if current_val + elem <= 0:
            curr_start = i
            curr_end = i+1
        else:
            current_val += elem
            curr_end    += 1
            if current_val > current_max:
                current_max = current_val
                max_start, max_end = curr_start, curr_end
    return array[max_start:max_end] #alternatives: max_start,max_end or current_max...        