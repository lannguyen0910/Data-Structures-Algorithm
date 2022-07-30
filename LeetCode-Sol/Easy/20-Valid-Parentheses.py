class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        d = {')':'(', '}':'{', ']':'['}
        for i in s:
            val = d.get(i)
            if stack and val == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        if stack:
            return False
        else:
            return True
