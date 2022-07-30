class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i):
            sum = informTime[i]
            if len(children[i]) > 0:
                sum += max([dfs(j) for j in children[i]])
            return sum
        # Build the adjacency list.
        children = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                children[m].append(i)
        return dfs(headID)

# source: https://docs.google.com/presentation/d/1F6xGHbgYPBeskd7HrNnlcky7ZMRPbk-wK2v7YpwXhRo/edit#slide=id.g13b4366fb05_0_268