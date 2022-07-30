class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        if not points or not queries:
            return []
        
        def is_inside(query, pt):
            distance = math.sqrt((query[0] - pt[0])**2 + (query[1] - pt[1])**2)
            return True if distance<=query[2] else False
        
        ret = []
        for query in queries:
            count = 0
            for pt in points:
                if is_inside(query, pt):
                    count+=1
            ret.append(count)
        
        return ret