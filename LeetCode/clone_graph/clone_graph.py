

class Node:
    """
    Definition for a Node.
    """

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        d = {}
        d[node.val] = Node(node.val)
        queue = []
        queue.append(node)

        while len(queue) != 0:
            cur_node = queue.pop(0)
            for neighbor in cur_node.neighbors:
                if neighbor.val not in d:
                    d[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                d[cur_node.val].neighbors.append(d[neighbor.val])

        return d[node.val]
