class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0]*26
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
            
        for i in count:
            if i !=0:
                return False
            
        return True
#     O(n)
#     Same for PALINDROME