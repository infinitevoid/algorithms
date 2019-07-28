from typing import List, Dict
from min_heap import MinHeap

class Node:
    __slots__ = ("left", "right", "freq", "char")
    def __init__(self, freq = None, char = None, left = None, right = None):
        self.char = char
        self.left, self.right = left, right
        self.freq = freq 
        if freq == None:
            self.freq = left.freq + right.freq
    def traverse(self, code = ""):
        if self.right == None:
            yield self.char, code
        else:
            yield from self.left.traverse(code + "0")
            yield from self.right.traverse(code + "1")
    def __gt__(self, node):
        return self.freq > node.freq 


def build_huffman_tree(letters: List[str], freq: List[int])->Node:
    heap = MinHeap(len(letters))
    for i,char in enumerate(letters):
        heap.insert(Node(freq[i], char))
    while len(heap) > 1:
        a = heap.pop()
        b = heap.pop()
        heap.insert(Node(left = a, right = b))
    return heap.pop()


def huffman_codes(root: Node)->Dict[str, str]:
    map = {}
    for char, code in root.traverse(""):
        map[char] = code
    return map

"""
###TODO###
if __name__ == "__main__":
    freq = [43,23,42,51,76]
    alph = ["a","b","c","d","e"]
    node = build_huffman_tree(alph, freq)
    map = huffman_codes(node)
    print(map)
"""