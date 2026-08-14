class ListNode:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.l = 0
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.hm = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hm:
            node = self.hm[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key].val = value
            self.get(key)
            return 
        if self.l == self.c:
            node = self.head.next
            self.head.next = node.next
            node.next.prev = self.head
            self.hm.pop(node.key)
            self.l -= 1
    
        node = ListNode(key, value, self.tail, self.tail.prev)
        self.tail.prev.next = node
        self.tail.prev = node
        self.hm[key] = node
            
        self.l += 1

        
