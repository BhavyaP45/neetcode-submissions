class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        t = 0
        b = m - 1
        row = -1
        if (m==1):
            row = 0

        while t <= b:
            mid =  t + (b - t)//2

            if matrix[mid][0] <= target and (mid == m - 1 or target < matrix[mid + 1][0]):
                row = mid
                break
            elif matrix[mid][0] > target:
                b = mid - 1
            else: 
                t = mid + 1
            
        if row == -1:
            return False
        
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


        
