# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def helper(root, arr, depth):
            arr.append(depth)
            if root.left:
                helper(root.left, arr, depth+1)
            if root.right:
                helper(root.right, arr, depth+1)
        arr = []
        helper(root, arr, 1)
        return max(arr)