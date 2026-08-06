class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i])) + "#"+ strs[i] 
        res += ""
        return res;
    def decode(self, s: str) -> List[str]:
        res = []
        len1 = 0
        if s == "":
            return []
        len2 = int(s[len1:s.find("#", len1)])
        lennum = s.find("#", len1) - len1

        while len2 != len(s) -1:
            if len1 == len2:
                res.append("")
            else:
                res.append(s[len1+ lennum + 1:len2+lennum + 1])
            len1 = len2 + lennum +1
            if s.find("#", len1) == -1:
                break
            len2 = int(s[len1:s.find("#", len1)]) + len1    
            lennum = s.find("#", len1) - len1
                

        return res
                
