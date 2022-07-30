# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_val= max(nums)
        idx = nums.index(max_val)
        
        root = TreeNode(val=max_val, left=None, right=None)
        
        
        def create_tree(nums, root, idx):
            left_arr = nums[:idx]
            right_arr = nums[idx+1:]
            
            if left_arr:
                max_val = max(left_arr)
                idx = left_arr.index(max_val)
                root.left = TreeNode(val=max_val, left=None, right=None)
                create_tree(left_arr, root.left, idx)
            
            if right_arr:
                max_val = max(right_arr)
                idx = right_arr.index(max_val)
                root.right = TreeNode(val=max_val, left=None, right=None)
                create_tree(right_arr, root.right, idx)
        
        create_tree(nums, root, idx)
        return root



# Faster - use dict to get loc w/ O(1)
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        # use dict to get location w/ O(1)        
        locations = dict()
        for i in range(len(nums)):
            locations[nums[i]] = i
        
        
        def helper(start, end):
            if start > end:  # base case 0: invalid
                return None
            elif start == end:  # base case 1: Just 1 element
                return TreeNode(nums[start])
            
            max_element = max(nums[start: end + 1])  # O(n): N will reduce each time
            max_index = locations[max_element]  # O(1) lookup
            
            root = TreeNode(max_element)
            root.left, root.right = helper(start, max_index - 1), helper(max_index + 1, end)
            return root
        
        return helper(0, len(nums) - 1)

