class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        operator = '+'
        operators = ['+', '-', '*', '/']
        nums = [str(i) for i in range(10)]

        for i, char in enumerate(s):
            if char in nums:
                res = res * 10 + int(char)

            if char in operators or i == len(s) - 1:
                if operator == '+':
                    stack.append(res)

                elif operator == '-':
                    stack.append(-res)

                elif operator == '*':

                    stack[-1] = int(stack[-1] * int(res))
                else:
                    stack[-1] = int(stack[-1] / int(res))

                res = 0
                operator = char

        return sum(stack)
