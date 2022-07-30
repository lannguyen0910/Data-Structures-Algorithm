# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        
        def traverse_inOrder(root, arr):
            if not root:
                return
            
            if low <= root.val and root.val <= high:
                arr.append(root.val)
            
            traverse_inOrder(root.left, arr)
            traverse_inOrder(root.right, arr)
        
        arr = []
        traverse_inOrder(root, arr)
        
        return sum(arr)