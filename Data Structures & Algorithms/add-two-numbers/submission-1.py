# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        f = l1
        s = l2
        nc = 0
        c = 0
        add = ListNode()
        curr = add
        
        while f or s:
            if f:
                a = f.val
                f = f.next
            else:
                a = 0
            if s:
                b = s.val
                s = s.next
            else:
                b = 0
            nc = (a + b + c) % 10
            c = (a + b + c) // 10
            curr.next = ListNode(nc)
            curr = curr.next
        if c:
            curr.next = ListNode(c)
            curr = curr.next
        return add.next
            
            

