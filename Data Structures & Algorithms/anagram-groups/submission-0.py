class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        hash_t = []
        for elem in strs:
            chars = [0] * 26
            for c in elem:
                chars[ord(c) - ord('a')] += 1
            if chars in hash_t:
                j = hash_t.index(chars)
                output[j].append(elem)
            else:
                output.append([elem])
                hash_t.append(chars)
            
        return output
        