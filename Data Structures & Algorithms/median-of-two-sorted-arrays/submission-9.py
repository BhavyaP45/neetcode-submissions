import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m = len(nums1)
        n = len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        
        l = 0
        r = m 
        med = nums2[-1]

        half = math.ceil((m + n) / 2)

        while l <= r:
            mid = l + (r-l )//2
            cut1 = mid 

            cut2 = half - mid 
            print(cut1, cut2)
            left1 = nums1[cut1 - 1] if cut1 >= 1 else float('-inf') 
            left2 = nums2[cut2 - 1] if cut2 >= 1 else float('-inf')
            right1 = nums1[cut1] if cut1 < m else float('inf')
            right2 = nums2[cut2] if cut2 < n else float('inf')
            print(left1, right2, left2, right1)
            if left1 <= right2 and left2 <= right1:
                med = max(left1, left2)
                if (m+n) % 2 == 0:
                    med = (max(left1, left2) + min(right1, right2) )/2
                return med
            elif left1 > right2:
                r = mid - 1
            else:
                l = mid + 1

        return med
        
