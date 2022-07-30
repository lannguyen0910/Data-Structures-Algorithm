class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        
        nums = nums1.copy()
        nums.update(nums2)
        nums.update(nums3)
        
        ret = []
        for val in nums:
            if val in nums1 and val in nums2:
                ret.append(val)
            elif val in nums2 and val in nums3:
                ret.append(val)
            elif val in nums1 and val in nums3:
                ret.append(val)
            
        return ret