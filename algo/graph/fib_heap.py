from typing import Any, List, Sequence

# implementation fibonacci heap

class DoublyLinkedList:
    pass
class LinkedNode:
    pass

class LinkedNode():
    __slots__ = ("parent","right","left","value")
    def __init__(self, parent: DoublyLinkedList, value: Any, right: LinkedNode = None, left: LinkedNode = None):
        self.parent = parent
        self.right = right
        self.left  = left
        self.value = value
    def remove(self):
        if self.left!=None:
            self.left.right = self.right
        else:
            self.parent.start = self.right

        if self.right!=None:
            self.right.left = self.left
        else:
            self.parent.end = self.left

class DoublyLinkedList():
    __slots__ = ("start","end")
    def __init__(self):
        self.start = None
        self.end = None
    def append(self, obj: Any):
        n = LinkedNode(self,obj)
        if self.start==None:
            self.start = n
            self.end = n
        else:
            self.end.right = n
            n.left = self.end
            self.end = n
    def clear(self):
        self.start = None
        self.end = None
    def iterate(self) -> Sequence[Any]:
        n = self.start
        while n!=None:
            yield n.value
            n = n.right


class FibNode():
    __slots__ = ("parent","container","children","degree","marked","handle","priority")
    def __init__(self, handle: Any, priority: float):
        self.parent = None
        self.container = None
        self.children = set()
        self.degree = 0
        self.marked = False
        self.handle = handle
        self.priority = priority
    

class FibonacciHeap():
    def __init__(self):
        self.root_list = DoublyLinkedList()
        self.nodes = {}
        self.smallest = None
        self.container = None
        self.total = 0

    def find_min(self) -> Any:
        if self.samllest != None:
            return self.smallest.handle
    def remove(self, handle: Any):
        self.decrease_priority(handle, float('-inf'))
        self.extract_min()
    
    def insert(self, handle: Any, priority: float):
        node = FibNode(handle,priority)
        self.nodes[handle] = node
        self.push(node)
        if (self.smallest ==  None) or (self.smallest.priority > node.priority):
            self.smallest = node
        self.total += 1

    def decrease_priority(self, handle: Any, value: float):
        node = self.nodes[handle]
        if value > node.priority:
            return
        node.priority = value
        self.cut(node)
        if node.priority<self.smallest.priority:
            self.smallest = node

    def cut(self,n: FibNode):
        if n.parent!=None:
            if n.parent.parent != None:
                if n.parent.marked:
                    self.cut(n.parent)
                else:
                    n.parent.marked = True
            else:
                n.parent.marked = False
            n.parent.children.remove(n)
            n.parent.degree -= 1
            self.push(n)
            n.parent = None
            n.marked = False

    def extract_min(self) -> Any:
        temp = self.smallest.handle
        for n in self.smallest.children:
            n.parent = None
            n.marked = False
            self.push(n)
        self.total -= 1
        self.smallest.container.remove()
        self.smallest = None
        self.cleanup()
        del self.nodes[temp]
        return temp

    def cleanup(self):
        arr = [None]*self.total
        for node in self.root_list.iterate():
            other = arr[node.degree]
            self.link(arr,node,other)
        self.root_list.clear()
        m = None
        for elem in arr:
            if elem!=None:
                self.push(elem)
                if (m==None) or (elem.priority<m.priority):
                    m = elem
        self.smallest = m

    def link(self, arr: List[FibNode], node: FibNode, other: FibNode):
        if other==None:
            arr[node.degree] = node 
        elif node.priority<other.priority:
            node.children.add(other)
            node.degree += 1
            other.parent = node
            arr[other.degree] = None
            self.link(arr,node,arr[node.degree])
        else:
            other.children.add(node)
            other.degree += 1
            node.parent = other
            arr[node.degree] = None
            self.link(arr,other,arr[other.degree])

    def push(self, n: FibNode):
        self.root_list.append(n)
        n.container = self.root_list.end

    def __len__(self) -> int:
        return self.total
    def __contains__(self, handle: Any) -> bool:
        return (handle in self.nodes.keys())

FibHeap = FibonacciHeap

    
