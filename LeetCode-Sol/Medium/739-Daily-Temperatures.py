class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0 or len(temperatures) == 1:
            return [0]
        
        stack = collections.deque()
        mydict = {}
        
        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            while stack and stack[-1][0] < temp:
                key, idx = stack.pop()
                val = i - idx
                mydict[idx] = val
            
            stack.append([temp, i])
        
        ret = [0]*len(temperatures)
        for idx, val in mydict.items():
            ret[idx] = val
        
        return ret