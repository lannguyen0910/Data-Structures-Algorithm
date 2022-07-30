# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        
        result = []
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        
        return ' '.join(result)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        dataQueue = collections.deque(data.split())
        root = TreeNode(int(dataQueue.popleft()))
        queue = collections.deque([root])

        while queue:
            parentNode = queue.popleft()
            childNode = dataQueue.popleft()

            if childNode != 'null':
                parentNode.left = TreeNode(int(childNode))
                queue.append(parentNode.left)
            else:
                parentNode.left = None
            
            childNode = dataQueue.popleft()
            if childNode != 'null':
                parentNode.right = TreeNode(int(childNode))
                queue.append(parentNode.right)
            else:
                parentNode.right = None

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))