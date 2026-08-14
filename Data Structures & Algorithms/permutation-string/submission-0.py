class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
        
        for r in range(len(s2)):
            count2[ord(s2[r]) - ord('a')] += 1

            if r >= len(s1)-1: 
                if count1 == count2:
                    return True
                
                count2[ord(s2[r - len(s1) + 1]) - ord('a')] -= 1
        
        return False

                
        