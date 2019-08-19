from typing import Dict, Any
from fib_heap import FibHeap as PriorityQueue

def prim_mst(graph: Dict[Any, Dict[Any, float]]):
    source = next(iter(graph))
    Q = PriorityQueue()
    for node in graph:
        Q.insert(node, float('inf'))
    Q.decrease_priority(source, 0)

    parent = {source: None}
    mst    = set()

    while len(Q) > 0:
        min = Q.extract_min()
        mst.add(min)
        for neighbor, dist in graph[min].items():
            if (neighbor not in mst)  and (dist < Q.get_priority(neighbor)):
                Q.decrease_priority(neighbor, dist)
                parent[neighbor] = min
    return parent

if __name__ == "__main__":
    graph = {"a": {"b": 10, "c": 30 ,"d": 50}, "b": {"c":15, "a":12, "d":25}, "c": {"a": 13, "d": 20}, "d":{"c": 13}}
    print(prim_mst(graph))
        
