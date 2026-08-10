# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        k = 0
        while tmp:
            tmp = tmp.next
            k += 1
        
        print(k)

        k2 = k - n

        print(k2)

        if k2 == 0:
            return head.next
        else:
            tmp = head

            while k2 > 1:
                tmp = tmp.next
                k2 -= 1
            print(tmp.val)

            tmp2 = tmp.next.next
            tmp.next = tmp2
            return head






