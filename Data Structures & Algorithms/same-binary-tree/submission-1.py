# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st1 = [p]
        st2 = [q]

        while st1:
            n1 = st1.pop()
            n2 = st2.pop()
            if not n1 and not n2:
                continue
            if (not n1 and n2) or (not n2 and n1) or n1.val != n2.val:
                return False

            st1.append(n1.left)
            st1.append(n1.right)
            st2.append(n2.left)
            st2.append(n2.right)
        
        return True




        
        