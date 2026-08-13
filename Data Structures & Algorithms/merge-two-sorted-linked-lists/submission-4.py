# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        p1 = list1
        p2 = list2

        if p1.val > p2.val:
            p2 = list1
            p1 = list2
        
        head = p1

        while p1:
            if not p1.next:
                p1.next = p2
                break
            
            p1nxt = p1.next
            while p2 and p1.val <= p2.val and p2.val < p1nxt.val:
                p2nxt = p2.next
                p1.next = p2
                p2.next = p1nxt
                p1 = p2
                p2 = p2nxt
            p1 = p1nxt

        return head
        