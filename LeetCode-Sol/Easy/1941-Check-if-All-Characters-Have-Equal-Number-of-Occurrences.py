class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_list = list(set(s))
        
        for i in range(1, len(char_list)):
            c1 = char_list[i-1]
            c2 = char_list[i]
            if s.count(c1) != s.count(c2):
                return False
        
        return True
            
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:  
        # Way 2: use dictionary
        d = defaultdict(int)
        
        for i in s:
            d[i]+=1
        
        fix_val = d.get(s[0])
        
        for key, val in d.items():
            if fix_val != val:
                return False
        
        return True
