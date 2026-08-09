import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        r = max(piles)
        l = 0

        min_spd = r

        while l <= r:
            spd = l + (r-l)//2
            if spd == 0:
                break
            running = 0
            for i in range(len(piles)):
                running += math.ceil(piles[i] / spd) if piles[i] > spd else 1
                if running > h:
                    break
            if running > h:
                l = spd + 1
            else: 
                r = spd - 1
                min_spd = min(min_spd, spd)
            print(spd)
        return min_spd



        
            