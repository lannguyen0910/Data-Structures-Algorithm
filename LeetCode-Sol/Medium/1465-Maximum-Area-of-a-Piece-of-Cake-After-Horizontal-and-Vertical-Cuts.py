class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        if not h or not w or not horizontalCuts or not verticalCuts:
            return 0
        
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = max_w = 0
        
        # find max h
        for h in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[h]-horizontalCuts[h-1])
            
        # find max w
        for w in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[w]-verticalCuts[w-1])
            
        return (max_h*max_w)%(10**9+7)
        
        