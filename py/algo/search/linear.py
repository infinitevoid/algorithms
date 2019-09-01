from typing import List,Any

def linear_search(array: List[Any], element: Any):
    for index,elem in enumerate(array):
        if elem == element:
            return index
    else:
        return -1

