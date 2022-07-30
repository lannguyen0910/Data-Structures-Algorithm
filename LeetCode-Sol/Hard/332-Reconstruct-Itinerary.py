class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # create graph
        graph = defaultdict(list)
        for depart, dest in tickets:
            heapq.heappush(graph[depart], dest)
              
        def dfs(graph, depart, arr):
            while graph[depart]:
                dest = heapq.heappop(graph[depart]) # dont need to check visited if use heappop
                dfs(graph, dest, arr)
            # must add at the end when src has no flights left
            arr.append(depart)

        ret = []
        dfs(graph, 'JFK', ret)        
        return reversed(ret)
    
    
# https://leetcode.com/problems/reconstruct-itinerary/discuss/2233444/Python-solution-with-15-lines-by-DFS
# https://leetcode.com/problems/reconstruct-itinerary/discuss/709699/Python-by-DFS-and-stack-w-Visualization

# Check info about Eulerian Path: https://www.youtube.com/watch?v=8MpoO2zA2l4