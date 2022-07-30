class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        
        nums.sort(reverse=True)
        return nums[k-1]