class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = defaultdict(int)
        
        if len(jewels) ==0 or len(stones) == 0:
            return 0
        
        ret = 0

        for c in jewels:
            ret += stones.count(c)
        
        
        return ret

class Solution_2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = defaultdict(int)
        
        if len(jewels) ==0 or len(stones) == 0:
            return 0
        
        for c in stones:
            d[c]+=1
        
        ret = 0
        
        for c in jewels:
            val = d.get(c) if d.get(c) else 0
            ret += val
        
        return ret

# Soln_1 is faster