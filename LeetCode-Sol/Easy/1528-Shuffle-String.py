class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret = ['']*len(s)
        
        if len(indices)!=len(s):
            return ''
        
        for i in range(len(s)):
            c = s[i]
            new_idx = indices[i]
            ret[new_idx] = c
        
        return ''.join(ret)