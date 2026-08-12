"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        hm = {None: None}
        if not ptr:
            return None
        while ptr:
            hm[ptr] = Node(ptr.val)
            ptr = ptr.next

        ptr = head
        while ptr:
            cur = hm[ptr]
            cur.next = hm[ptr.next] 
            cur.random = hm[ptr.random]
            ptr = ptr.next
        
        return hm[head]







        