class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        n = n.replace('0b','')
        n = n.zfill(32)
        
        lst = list(n)
        return lst.count('1')