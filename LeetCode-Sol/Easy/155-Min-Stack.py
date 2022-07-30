class MinStack:

    def __init__(self):
        self.stack = []
        self.min_s = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.min_s):
            min_data = self.min_s[-1]
            self.min_s.append(val if val < min_data else min_data)
        else:
            self.min_s.append(val)
            
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_s.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_s:
            return self.min_s[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()