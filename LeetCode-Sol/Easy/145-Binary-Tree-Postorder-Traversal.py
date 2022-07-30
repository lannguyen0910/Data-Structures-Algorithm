# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        ret = []
        def dfs(root, arr):
            if not root:
                return
            dfs(root.left, arr)
            dfs(root.right, arr)
            arr.append(root.val)

            return arr
        
        arr = []
        ret = dfs(root, arr)
        return ret