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
        if not head:
            return None
        new_head = Node(head.val, head.next, head.random)
        hm = {head: new_head}

        while ptr:
            if ptr.next and ptr.next not in hm:
                hm[ptr.next] = Node(ptr.next.val)
            hm[ptr].next = hm[ptr.next] if ptr.next else None
            if ptr.random and ptr.random not in hm:
                hm[ptr.random] = Node(ptr.random.val)
            hm[ptr].random = hm[ptr.random] if ptr.random else None
            ptr = ptr.next
            
        return new_head





        