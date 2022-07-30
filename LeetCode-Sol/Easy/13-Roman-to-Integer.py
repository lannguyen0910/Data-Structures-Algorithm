class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 
             'V':5, 
             'X':10, 
             'L':50, 
             'C':100, 
             'D':500, 
             'M':1000
            }
        d1 = {'IV':4,
             'IX':9,
             'XL':40,
             'XC':90,
             'CD':400,
             'CM':900
             }
        ret = 0
        
        for i in d1.keys():
            ret += s.count(i) * d1.get(i)
            s = s.replace(i, '')
            
        for i in d.keys():
            ret += s.count(i) * d.get(i)
        
        return ret