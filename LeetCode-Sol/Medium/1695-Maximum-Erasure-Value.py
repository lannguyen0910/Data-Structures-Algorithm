class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        left = right = ret_sum = local_sum = 0
        seen = set()
        
        for right in range(len(nums)):
            val = nums[right]
            while val in seen and left < right:
                local_sum -= nums[left]
                seen.remove(nums[left])
                left += 1
            
            seen.add(val)
            local_sum += val
            ret_sum = max(ret_sum, local_sum)
        
        return ret_sum
    
