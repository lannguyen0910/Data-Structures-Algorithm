class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if len(products)==0 or len(searchWord)==0:
            return []
        
        products.sort()
        keyWord = []
        
        for i in range(1, len(searchWord)+1):
            keyWord.append(searchWord[:i])
            
        ret = []
        for key in keyWord:
            l = []
            for s in products:
                if s.startswith(key) and len(l)<3:
                    l.append(s)
            ret.append(l)
            
        return ret