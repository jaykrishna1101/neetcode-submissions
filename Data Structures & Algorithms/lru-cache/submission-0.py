class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.d:
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])
        self.d[key] = Node(key, value)
        self.insert(self.d[key])

        if len(self.d) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.d[lru.key]

        
        
