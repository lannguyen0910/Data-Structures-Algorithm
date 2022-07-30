class Solution:
    def decodeString(self, s: str) -> str:
        # S: Stack for tracking the "outside" of the current nested expression.
        stack = []
      
        # cur: tracking the "inside" of the current nested expression.
        cur = [0, '']
      
        for c in s:
            if c == '[':
                # Enter a new loop:
                # Reset the current expression.
                stack.append(cur)
                cur = [0, '']
            elif c == ']':
                # Exit from the loop:
                # Pop out the stack to recall the "outside" of the current expression
                # and merge the current expression to it.
                num, prev_str = stack.pop()
                cur[1] = prev_str + num*cur[1]
            elif c.isdigit():
                # Digits:
                # Adding the digit into the current expression.
                cur[0] *= 10
                cur[0] += int(c)
            else:
                # Characters:
                # Adding the character into the current expression.
                cur[1] += c
      
        return cur[1]