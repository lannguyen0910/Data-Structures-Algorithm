class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        
        heap = []
        for key, val in d.items():
            heapq.heappush(heap, (-val, key))
        
        ret = ''
        while len(heap)>0:
            val, key = heapq.heappop(heap)
            ret = ret + (key*(-val))
        
        return ret