# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        d = defaultdict(list)
        
        def helper(root, d, depth):
            d[depth].append(root.val)
            if root.left:
                helper(root.left, d, depth+1)
            if root.right:
                helper(root.right, d, depth+1)
                
        helper(root, d, 0)
        
        sorted_key = sorted(d.keys())
        ret = [d.get(val) for val in sorted_key]
        return ret
        