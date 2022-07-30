class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        # Way 1: use dict -> filter out those has count >1
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        
        ret = 0
        
        for key, val in d.items():
            if val == 1:
                ret += key
        
        return ret
        
        # Way 2: loop through ele, total+=ele, if ele in set -> total-=ele