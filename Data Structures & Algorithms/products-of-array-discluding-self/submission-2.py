class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        res = []

        for i in range(0, len(nums)-1):
            left.append(left[i] * nums[i])
        
        for i in range(len(nums) - 1, 0, -1):
            right.append(right[len(nums) -1 -i] * nums[i])
        right.reverse()

        for i in range(len(nums)):
            res.append(left[i] * right[i])
        
        return res
        