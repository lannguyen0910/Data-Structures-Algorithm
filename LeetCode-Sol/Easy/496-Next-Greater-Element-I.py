class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mymap = {}
        stack = collections.deque()
        
        for num in nums2:
            while stack and stack[-1] < num:
                mymap[stack.pop()] = num
            stack.append(num)
        
        ret = []
        for num in nums1:
            val = mymap.get(num)
            if val is None:
                ret.append(-1)
            else:
                ret.append(val)
        
        
        return ret
    
