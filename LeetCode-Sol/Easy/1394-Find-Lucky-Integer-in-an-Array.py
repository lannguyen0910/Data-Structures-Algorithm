class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = defaultdict(int)
        
        # add integer + its frequency into dict
        for i in arr:
            d[i] += 1
        
        ret = -1
        
        # check if key==freq
        # update ret if yes
        for key, val in d.items():
            if key == val:
                ret = max(ret, key)
        
        return ret
        
        