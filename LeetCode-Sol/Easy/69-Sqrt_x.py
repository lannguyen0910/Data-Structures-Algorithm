class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x == 1:
            return x
        for i in range(x+1):
            val = i*i
            if val == x:
                return i
            if val>x:
                return i-1
