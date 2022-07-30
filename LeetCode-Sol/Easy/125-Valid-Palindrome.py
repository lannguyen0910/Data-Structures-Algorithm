class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = re.findall(r"[a-z0-9]", s.lower())
        x = ''.join(x)
        
        if len(x)==0:
            return True
        
        p1 = 0
        p2 = len(x)-1
        while True:
            if x[p1] != x[p2]:
                return False
            elif p1 == p2 or p1>p2:
                return True
            else:
                p1 += 1
                p2 -= 1
        
