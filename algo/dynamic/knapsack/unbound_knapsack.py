from typing import List

def unbounded_knapsack(capacity: int, weights: List[int], values: List[int]):
    n = len(values)
    dp = [0 for i in range(capacity+1)]
    dp[0] = 0
    for cap in range(capacity+1):
        for i in range(n):
            if(weights[i] <= cap):
                dp[cap] = max(dp[cap], values[i] + dp[cap-weights[i]])
    return dp[capacity]


"""
###Test###
if __name__ == "__main__":
    val = [60, 100, 120]  
    wt = [10, 20, 30]  
    W = 50
    print(unbounded_knapsack(W, wt, val))
"""