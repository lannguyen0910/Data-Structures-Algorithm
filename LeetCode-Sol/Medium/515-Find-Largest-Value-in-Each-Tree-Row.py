# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        d = defaultdict(list)
        ret = [root.val]
        
        def helper(root, height):
            if not root:
                return
            
            # add into return arr new height, init w/ min val
            if len(ret) < height+1:
                ret.append(float('-inf'))
            # update max val in height
            ret[height] = max(ret[height], root.val)
            
            # continue next height
            helper(root.left, height+1)
            helper(root.right, height+1)
            
        helper(root, 0)
        
        return ret
