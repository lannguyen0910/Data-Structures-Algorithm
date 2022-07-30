# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]) -> None:
        # return inorder traversal
        if root is None:
            return []
        return self.inOrderTraversal(root.left) + [root] + self.inOrderTraversal(root.right) 


    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        tmp_arr = []
        arr = self.inOrderTraversal(root)

        
        for i in range(len(arr)-1):
            prev_node = arr[i]
            curr_node = arr[i+1]
            # find the pair needed to swap
            if prev_node.val > curr_node.val:
                # find smallest node to the right of node i and swap this node with smallest
                minNode = min(arr[i+1:], key=lambda node: node.val)
                arr[i].val, minNode.val = minNode.val, arr[i].val

        
# https://leetcode.com/problems/recover-binary-search-tree/discuss/2156432/python-easy-to-understand