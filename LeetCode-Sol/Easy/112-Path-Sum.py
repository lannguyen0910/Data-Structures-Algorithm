# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        targetSum = targetSum - root.val
        
        # base case
        if not root.left and not root.right:
            return targetSum == 0
        
        # recursive case
        if root.left and self.hasPathSum(root.left, targetSum):
            return True
        
        if root.right and self.hasPathSum(root.right, targetSum): 
            return True
        
        return False
