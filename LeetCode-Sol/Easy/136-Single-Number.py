class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        
        for i in nums:
            d[i]+=1
            
        for key, val in d.items():
            if val==1:
                return key