# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root, arr):
            if not root:
                return []
            arr.append(root.val)
            dfs(root.left, arr)
            dfs(root.right, arr)
            
            return arr
        
        arr = []
        return dfs(root, arr)
