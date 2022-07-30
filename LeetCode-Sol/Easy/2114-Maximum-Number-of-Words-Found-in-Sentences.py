class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ret = 0
        if not sentences:
            return ret
        
        for sen in sentences:
            ret = max(ret, len(sen.split()))
            
        return ret
