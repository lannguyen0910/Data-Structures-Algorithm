class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = sys.maxsize
        min_str = ''
        
        for s in strs:
            if len(s)<min_len:
                min_len = len(s)
                min_str = s
        
        for i in range(min_len):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return s[0:i]
        return min_str