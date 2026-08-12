class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l =  mid + 1
            else:
                r = mid
        
        r1 = l - 1 if l > 0 else 0
        l2 = l if l > 0 else l+1

        for l, r in [(0, r1), (l2, len(nums) - 1)]:
            while l <= r:
                print(l, r)
                m = l + (r-l)//2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else: 
                    r = m - 1

        return -1



        