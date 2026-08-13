class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l+= 1
            maxp = max(maxp, prices[r] - prices[l])
        
        return maxp

        