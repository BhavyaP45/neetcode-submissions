class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):

            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                last_day = stack[-1]
                res[last_day] = i - last_day
                stack.pop()
            stack.append(i)      
        return res