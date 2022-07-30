class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        
        # use BFS
        visited = set()
        queue = deque()
        queue.append(0)
        
        while queue:
            curr = queue.popleft()
            
            # do nothing if visited
            if curr in visited: continue
            else:
                visited.add(curr)
                key_list = rooms[curr]
                for key in key_list:
                    queue.append(key)
        
        
        return len(visited)==len(rooms)

    # O(V+E)