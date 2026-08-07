class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:

            if maxLeft < maxRight:
                l += 1
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    res += maxLeft - height[l] 
            else:
                r -= 1
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    res += maxRight - height[r] 
            
        return res

