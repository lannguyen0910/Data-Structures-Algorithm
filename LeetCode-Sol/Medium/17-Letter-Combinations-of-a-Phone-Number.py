class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']        
        ret = []
        
        if not digits:
            return ret
        
        def helper(s: str, arr):
            ret1 = []
            for word in arr:
                for c in s:
                    ret1.append(word + c)
            return ret1
        
        for val in digits:
            val = int(val)

            s = arr[val]
            if len(ret)==0:
                for c in s:
                    ret.append(c)
            else:
                ret = helper(s, ret)
      
        return ret