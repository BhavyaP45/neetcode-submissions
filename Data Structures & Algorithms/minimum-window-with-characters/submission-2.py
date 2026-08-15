class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res = ""
        freqt = {}
        for i in range(len(t)):
            freqt[t[i]] = freqt.get(t[i], 0) + 1
        
        l = 0
        have, need = 0, len(freqt)

        freqs = {}
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            if s[r] in freqt and freqs[s[r]] == freqt[s[r]]:
                have += 1
            
            while have == need:
                    if res == "" or len(res) > r - l + 1:
                        res = s[l: r+ 1]
                    freqs[s[l]] -= 1
                    if s[l] in freqt and freqs[s[l]] < freqt[s[l]]:
                        have -= 1
                    l += 1
        return res


        
        