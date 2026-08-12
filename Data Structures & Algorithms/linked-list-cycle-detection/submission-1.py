# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = set()
        ptr = head
        while ptr:
            if ptr.next in hm:
                
                return True
            hm.add(ptr.next)
            ptr = ptr.next

        return False



        
        