class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        gaps = defaultdict(int)
        for bricks in wall:
            gap = 0
            for brick in bricks[:-1]:
                gap += brick
                gaps[gap] +=1
        
        maxGaps = max(list(gaps.values())) if gaps else 0
        return len(wall) - maxGaps

class Solution_2:
    def leastBricks(self, wall: List[List[int]]) -> int:
        l = []
        total_count = 0
        for row in wall:
            queue = collections.deque()
            count = 0
            for brck in row:
                count += brck
                queue.append(count)
            
            total_count = count
            l.append(queue)
        
        min_val = 99999
        for i in range(total_count):
            count = 0
            for row in range(len(l)):
                curr_queue = l[row]
                if curr_queue and i == curr_queue[0]:
                    count += 1
                    curr_queue.popleft()
            
            min_val = min(min_val, len(l)-count)
        
        return min_val
      