class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # add edges into dict (node -> neighbors)
        graph = collections.defaultdict(set)
        for v1,v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        # add nodes with 1 neighbor into leaves
        leaves = collections.deque()
        for v, neighbors in graph.items():
            if len(neighbors) == 1:
                leaves.append(v)
        
        
        while n > 2:
            size = len(leaves)
            n -= size
            
            # check through each leaf node
            for i in range(size):
                
                # get leaf and its neighbor
                leave = leaves.popleft()
                neighbors = graph[leave]
                
                # check each neighbor
                for neighbor in neighbors:
                    # remove node leaf from all neighbors
                    graph[neighbor].remove(leave)
                    if len(graph[neighbor]) == 1:
                        leaves.append(neighbor)
        return leaves

# https://leetcode.com/problems/minimum-height-trees/discuss/729639/easy-python
        
        