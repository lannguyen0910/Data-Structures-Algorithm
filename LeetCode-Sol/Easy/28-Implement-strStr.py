class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        if needle not in haystack:
            return -1
        
        return haystack.index(needle)