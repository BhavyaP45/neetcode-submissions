class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = l
        chars = set()
        maxlen = 0
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                maxlen = max(maxlen, r - l + 1)
                r += 1
            else:
                chars.remove(s[l])
                l+= 1
        return maxlen


        