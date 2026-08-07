class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
        if len(s) % 2 != 0:
            return False
        par = {'(': ')', '{': '}', '[': ']'}
        for i in range(len(s)):
            if s[i] in {'(', '{', '['}:
                stack.append(s[i])
            elif len(stack) == 0 or s[i] != par[stack[-1]]:
                return False
            elif s[i] == par[stack[-1]]:
                stack.pop()
        if len(stack) == 0:
            return True
        else: 
            return False