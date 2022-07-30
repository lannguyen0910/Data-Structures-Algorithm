class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        start = 0
        end = 10
        mymap = collections.defaultdict(int)
        ret = []
        while end <= len(s):
            sub = s[start:end]
            mymap[sub]+=1
            if mymap[sub]>1:
                ret.append(sub)
            start += 1
            end += 1
        return list(set(ret))