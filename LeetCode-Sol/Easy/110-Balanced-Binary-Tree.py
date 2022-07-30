# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.balance = True
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
                
        def height(root):
            if not root:
                return 0
            
            lh = height(root.left)
            rh = height(root.right)
            
            gap = abs(lh- rh)
            if gap>1:
                self.balance = False
            
            return max(lh, rh) + 1

        height(root)
        return self.balance