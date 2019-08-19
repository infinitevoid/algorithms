from typing import List

def knapsack_01(capacity: int, weights: List[int], values: List[int]):
    n = len(values)
    row = [0 for i in range(capacity+1)]
    table = [row[:] for j in range(n+1)]

    for i in range(n+1):
        for cap in range(capacity+1):
            if cap == 0 or i == 0:
                table[i][cap] = 0
            elif weights[i-1] <= cap:
                table[i][cap] = max(table[i-1][cap], values[i-1] + table[i-1][cap-weights[i-1]])
            else:
                table[i][cap] = table[i-1][cap]
    return table[n][capacity]

"""
###Test###
if __name__ == "__main__":
    val = [60, 100, 120]  
    wt = [10, 20, 30]  
    W = 50
    print(knapsack_01(W, wt, val))
"""