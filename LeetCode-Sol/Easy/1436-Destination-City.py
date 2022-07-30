class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for src, end in paths:
            d[src] = end
        
        start = paths[0][0]
        
        curr = start
        cities = set(d.keys())
        while curr in cities and d[curr]:
            curr = d[curr]
            
        return curr
    