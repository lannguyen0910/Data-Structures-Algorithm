# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        d = defaultdict(int)
        
        def cal_sum(root, d):
            left_val = 0
            right_val = 0
            
            # calculate sum of left & right children
            if root.left:
                left_val += cal_sum(root.left, d)
            if root.right:
                right_val += cal_sum(root.right, d)
            
            total = root.val + left_val + right_val
            d[total] += 1
            
            return total
        
        cal_sum(root, d)
        max_freq = max(d.values())
        ret = []
        for key, val in d.items():
            if val == max_freq:
                ret.append(key)
        
        return ret