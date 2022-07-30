class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs)==0:
            return []
        
        d = collections.defaultdict(list)
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            d[tuple(arr)].append(s)  # dict: key=tuple - value=list
    
        ret = []
        for key in d.keys():
            ret.append(d[key])
        
        return ret