class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n=len(graph)
        clr=[-1]*n
        vis=[False]*n

        def dfs(src,vis, graph):
            vis[src]=True
            for u in graph[src]:
                if not vis[u]:
                    clr[u]=-1*clr[src]
                    if not dfs(u,vis, graph):
                        return False
                else:
                    if clr[src]==clr[u]:
                        return False
            return True

        for i in range(len(graph)):
            if not vis[i]:
                if not dfs(i,vis, graph):
                    return False
        
        return True