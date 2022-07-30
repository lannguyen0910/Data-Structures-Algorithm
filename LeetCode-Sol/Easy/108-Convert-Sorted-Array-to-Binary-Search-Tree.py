# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums)==1:
            return TreeNode(val=nums[0], left=None, right=None)
        
        def helper(nums):
            if not nums:
                return None
            
            mid = len(nums)//2
            curr = TreeNode(nums[mid])
            
            curr.left = helper(nums[:mid])
            curr.right = helper(nums[mid+1:])
            
            return curr
        
        return helper(nums)
