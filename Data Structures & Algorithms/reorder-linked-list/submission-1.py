# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        ptr = head
        l = 0
        while ptr:
            l += 1
            ptr = ptr.next
        
        half = (l+1)//2
        ptr = head
        i = 0
        while ptr:
            if i >= half:
                stack.append(ptr)
            ptr = ptr.next
            i += 1
        ptr = head
        while stack:
            nextptr = ptr.next
            n = stack.pop()
            ptr.next = n
            n.next = nextptr
            ptr = nextptr

        ptr.next = None       
        


