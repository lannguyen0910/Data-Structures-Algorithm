class Solution_1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        tmp = []
        for i in points:
            val = math.sqrt(i[0]**2 + i[1]**2)
            heapq.heappush(tmp, (val, i))

        for i in range(k):
            result.append(heapq.heappop(tmp)[1])

        return result

class Solution_2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        tmp = []
        
        if k==0:
            return result
        if k >= len(points):
            return points
        
        for i in points:
            val = math.sqrt(i[0]**2 + i[1]**2)
            heapq.heappush(tmp, (val, i))

        for i in range(k):
            result.append(heapq.heappop(tmp)[1])

        return result

class Solution_3:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        tmp = []
        
        if k==0:
            return result
        if k >= len(points):
            return points
        
        for i in points:
            val = - math.sqrt(i[0]**2 + i[1]**2)
            heapq.heappush(tmp, (val, i))
            if len(tmp) > k:
                heapq.heappop(tmp)
                
        for i in tmp:
            result.append(i[1])

        return result