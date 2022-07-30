# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse_preorder(root, arr):
            if not root:
                return
            
            arr.append(root)
            left = root.left
            right = root.right
            root.left = None
            root.right = None
            traverse_preorder(left, arr)
            traverse_preorder(right, arr)
        
        arr = []
        traverse_preorder(root, arr)
        
        for i in range(1, len(arr)+1):
            prevNode = arr[i-1]
            currNode = arr[i] if i < len(arr) else None

            prevNode.right = currNode 