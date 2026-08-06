class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            l = i + 1
            r = len(nums)  - 1
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            while l < r:
                if (nums[i] == -(nums[l] + nums[r])):
                    res.append([nums[i], nums[l], nums[r]])
                    while l < len(nums)-1 and nums[l] == nums[l+1]:
                        l += 1
                    while r > 1 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif (nums[i] < -(nums[l] + nums[r])):
                    l +=1 
                else:
                    r -= 1
            i += 1
        return res

