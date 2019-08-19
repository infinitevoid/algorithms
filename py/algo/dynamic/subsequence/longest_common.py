from typing import List, Any

def down_to(value, limit):
    for i in range(value, limit - 1, -1): yield i

def longest_common_subsequence(a: List[Any], b: List[Any]):
    row   = [0 for i in range(len(a) + 1)]
    table = [row[:] for j in range(len(b) + 1)]
    for i in down_to(len(a), 0):
        for j in down_to(len(b), 0):
            if i == len(a) or j == len(b):
                table[j][i] = 0 
            elif a[i] == b[j]:
                table[j][i] = 1 + table[j+1][i+1]
            else:
                table[j][i] = max(table[j+1][i], table[j][i+1])
    return table[0][0]


def lcs_rec(a: List[Any], b: List[Any], i: int = 0, j: int = 0):
    if i >= len(a) or j >= len(b):
        return 0
    elif a[i] == b[j]:
        return 1 + lcs_rec(a, b, i + 1, j + 1)
    else:
        return max(lcs_rec(a, b, i + 1, j), lcs_rec(a, b, i, j + 1))
"""
###Test###
if __name__ == "__main__":
    a = "AGGTAB";  
    b = "GXTXAYB";  
    print(longest_common_subsequence(a,b))
    print(lcs_rec(a,b))
"""