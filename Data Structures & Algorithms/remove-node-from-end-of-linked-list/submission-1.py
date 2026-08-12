# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        l = 0
        while ptr:
            l += 1
            ptr = ptr.next
        
        ptr = head

        if l == 1:
            return None
        elif l == n:
            return ptr.next

        while l > n + 1:
            ptr = ptr.next
            l -= 1
        cur = ptr.next
        ptr.next = cur.next if cur else None
        return head

