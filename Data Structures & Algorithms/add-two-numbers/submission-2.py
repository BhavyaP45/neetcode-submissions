# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2

        while p1:
            if not p1.next and p2 and p2.next:
                p1.next = ListNode()

            s = p1.val + p2.val if p2 else p1.val
            p1.val = s % 10

            if s//10:
                if not p1.next:
                    p1.next = ListNode()
                p1.next.val += 1
            

            p1 = p1.next
            p2 = p2.next if p2 else None
        
        return l1
        



        