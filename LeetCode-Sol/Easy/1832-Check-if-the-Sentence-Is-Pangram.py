class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = defaultdict(int)
        
        for i in sentence:
            d[i]+=1
        
        arr = list(d.keys())
        
        return len(arr)==26
