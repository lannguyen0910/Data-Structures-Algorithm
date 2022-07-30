class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)
        n = n.replace('0b','')
        n = n.zfill(32)
        
        
        lst = list(n)
        lst.reverse()

        lst.insert(0,'0b')

        return int(''.join(lst),2)