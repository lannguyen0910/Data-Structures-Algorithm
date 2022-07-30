# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        
        def inOrderTraverse(root, depth, loc):
            if not root.left and not root.right:
                d[depth].append((loc, root.val))
            if root.left:
                inOrderTraverse(root.left, depth+1, loc-1)
            if root.right:
                inOrderTraverse(root.right, depth+1, loc+1)
            
        inOrderTraverse(root, 0, 0)
        
        # get deepest
        deepest = max(d.keys())
        
        # find leftmost
        leftmost_key = sys.maxsize
        leftmost_val = 0
        for left, val in d[deepest]:
            if left < leftmost_key:
                leftmost_key = left
                leftmost_val = val
        
        return leftmost_val
        