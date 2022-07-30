# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        def inOrder_traverse(root, arr):
            if root.left:
                inOrder_traverse(root.left, arr)
            arr.append(root.val)
            if root.right:
                inOrder_traverse(root.right, arr)
                
        arr = []
        inOrder_traverse(root, arr)
        arr.sort()
        return arr[k-1]
                
                