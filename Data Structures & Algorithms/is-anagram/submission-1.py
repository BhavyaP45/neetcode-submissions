class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = [0] * 26
        t_char = [0] * 26

        for c in s:
            s_char[ord(c) - ord('a')] += 1
        for c in t:
            t_char[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if s_char[i] != t_char[i]:
                return False
        return True

        