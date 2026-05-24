class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        maxl = 1
        count = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                count +=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                count = 1
            
            if count > maxl:
                maxl = count

        return maxl






        