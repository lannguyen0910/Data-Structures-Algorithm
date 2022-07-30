class Solution:
    def reverse(self, x: int) -> int:
        s = ''
        if x == 0:
            return 0
        
        sign = x / abs(x)
        s = str(abs(x))[::-1]
        
        ret = sign *  int(s)
        ret = int(ret)
        return ret if ret < math.pow(2, 31) and ret >= -1*math.pow(2, 31) else 0