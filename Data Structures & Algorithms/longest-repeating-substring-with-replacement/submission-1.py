class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        max_freq = 0
        mlen = 0
        l = 0

        for r in range(len(s)):
            if s[r] not in hm:
                hm[s[r]] = 1
            else:
                hm[s[r]] += 1
            
            max_freq = max(max_freq, hm[s[r]])

            while r - l + 1 - max_freq > k:
                hm[s[l]] -= 1
                l += 1
                
            mlen = max(mlen, r - l + 1)
               
        return mlen