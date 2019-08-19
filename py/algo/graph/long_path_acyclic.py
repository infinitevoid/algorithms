from typing import Dict, Any

def dfs(graph, node, visited, dp):
    visited[node] = True
    res = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, dp)
        res = max(res, 1+dp[neighbor])
    dp[node] = res
        

def longest_path_acyclic(graph: Dict[Any, Dict[Any, float]]):
    dp = {}
    visited = { n:False for n in graph}
    for node in graph:
        if not visited[node]:
            dfs(graph, node, visited, dp)
    m = 0
    for key, val in dp.items():
        if val > m: m = val
    return m

if __name__ == "__main__":
    graph = {1: [2, 3], 2: [4], 3:[2, 4], 4:[]}
    print(longest_path_acyclic(graph))