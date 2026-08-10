"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None : None}
        n = head

        while n:
            temp = Node(n.val)
            d[n] = temp
            n = n.next

        n = head
        while n:
            temp = d[n]
            temp.next = d[n.next]
            temp.random = d[n.random]
            n = n.next
        
        return d[head]



