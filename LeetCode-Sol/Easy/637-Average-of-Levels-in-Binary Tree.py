# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        sum_lvl = [root.val]
        count_lvl = [1]
        
        def helper(root, curr_lvl, sum_lvl, count_lvl):
            
            if len(sum_lvl)<=curr_lvl:
                sum_lvl.append(root.val)
                count_lvl.append(1)
            else:
                sum_lvl[curr_lvl] += root.val
                count_lvl[curr_lvl] += 1
                
            if root.left:
                helper(root.left, curr_lvl+1, sum_lvl, count_lvl)
            if root.right:
                helper(root.right, curr_lvl+1, sum_lvl, count_lvl)
        
        
        helper(root, 0, sum_lvl, count_lvl)
        ret = [total/count for total, count in zip(sum_lvl, count_lvl)]
        
        return ret
        