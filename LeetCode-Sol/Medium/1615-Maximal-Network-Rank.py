class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # init graph
        graph = {}
        for i in range(n):
            graph[i] = set()
        
        # add vertices into graph
        for src, dest in roads:
            graph[src].add(dest)
            graph[dest].add(src)
        
        # return value
        ret_max = 0
        
        # check each pair of cities
        for city_1 in range(n):
            for city_2 in range(city_1+1,n):
                curr_rank = len(graph[city_1]) + len(graph[city_2])
                
                # remove overlapping route b/w 2 cities
                if city_1 in graph[city_2]:
                    curr_rank -= 1
                    
                # update max rank
                ret_max = max(ret_max, curr_rank)
        
        return ret_max
        