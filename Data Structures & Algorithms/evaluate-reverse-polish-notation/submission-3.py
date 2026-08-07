class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            val = tokens[i]

            if val in {'+', '-', '*', '/'}:
                res = 0
                second_val = stack.pop()
                first_val = stack.pop()
                if val == '+':
                    res = first_val + second_val
                elif val == '-':
                    res = first_val - second_val
                elif val == '*':
                    res = first_val * second_val
                else:
                    res = int(first_val / second_val)
                
                stack.append(res)

            else:
                stack.append(int(val))    

        return stack[-1]


        