from typing import Dict, Any
from fib_heap import FibHeap as PriorityQueue



def dijkstra(graph: Dict[Any, Dict[Any, float]], source: Any):
    Q = PriorityQueue()
    dist, prev = {}, {}
    for node in graph:
        Q.insert(node, float('inf'))
        dist[node] = float('inf')
    Q.decrease_priority(source, 0)
    dist[source] = 0

    while len(Q) > 0:
        min = Q.extract_min()
        for neighbor, delta in graph[min].items():
            new_dist = dist[min] + delta
            if neighbor in Q and new_dist < dist[neighbor]:
                Q.decrease_priority(neighbor, new_dist)
                dist[neighbor] = new_dist
                prev[neighbor] = min

    return prev, dist

    
if __name__ == "__main__":
    graph = {"a": {"b": 10, "c": 30 ,"d": 50}, "b": {"c":15, "a":12, "d":25}, "c": {"a": 13, "d": 20}, "d":{"c": 13}}
    print(dijkstra(graph, "a"))