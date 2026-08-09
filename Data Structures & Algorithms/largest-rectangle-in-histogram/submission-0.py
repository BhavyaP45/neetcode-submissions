class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0    
        stack = []

        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
                continue
            
            while stack and heights[i] <= heights[stack[-1]]:
                l = stack.pop()
                h = heights[l]
                width = i - stack[-1] - 1 if stack else i
                max_area = max(max_area, width * h)
            stack.append(i)
        while stack:
            j = stack.pop()
            h = heights[j]
            width = len(heights) - stack[-1] - 1 if stack else len(heights)
            max_area = max(max_area, h * width)
        return max_area



        
            
            