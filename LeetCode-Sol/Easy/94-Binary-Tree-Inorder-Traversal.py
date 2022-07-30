# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def go_depth(self, root, arr):
        if root.left:
            self.go_depth(root.left, arr)
        arr.append(root.val)
        if root.right:
            self.go_depth(root.right, arr)
        return arr
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        tmp = []
        arr = self.go_depth(root, tmp)
        
        return arr
