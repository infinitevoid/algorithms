from typing import List, Dict
from heapq import heapify, heappop, heappush

class Node:
    __slots__ = ("left", "right", "char")
    def __init__(self, char = None, left = None, right = None):
        self.char = char
        self.left, self.right = left, right
    def traverse(self, code = ""):
        if self.right == None:
            yield self.char, code
        else:
            yield from self.left.traverse(code + "0")
            yield from self.right.traverse(code + "1")


def build_huffman_tree(letters: List[str], freq: List[int])->Node:
    heap = [(freq[i], Node(letters[i])) for  i in range(len(letters))]
    heapify(heap)
    while len(heap) > 1:
        fa,a = heappop(heap)
        fb,b = heappop(heap)
        heappush(heap, (fa+fb, Node(left = a, right = b)))
    return heappop(heap)[1]


def huffman_codes(root: Node)->Dict[str, str]:
    map = {}
    for char, code in root.traverse(""):
        map[char] = code
    return map


###TODO###
if __name__ == "__main__":
    freq = [43,23,42,51,76]
    alph = ["a","b","c","d","e"]
    node = build_huffman_tree(alph, freq)
    map = huffman_codes(node)
    print(map)
