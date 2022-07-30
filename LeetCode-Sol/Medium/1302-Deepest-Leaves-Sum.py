# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        d = defaultdict(list)
        
        def helper(root, depth):
            if not root:
                return
            d[depth].append(root.val)
            
            helper(root.left, depth+1)
            helper(root.right, depth+1)
        
        helper(root, 0)
        
        max_depth = max(d.keys())
        return sum(d[max_depth])