class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if not cardPoints:
            return 0
        if len(cardPoints)==k:
            return sum(cardPoints)
        
        
        total_sum = sum(cardPoints)
        start = 0
        end = start + (len(cardPoints) - k)
        curr_sum = sum(cardPoints[start:end])
  
        ret = max(total_sum - curr_sum, 0)
        
        while end < len(cardPoints):

            curr_sum -= cardPoints[start]
            curr_sum += cardPoints[end]
            ret = max(total_sum - curr_sum, ret)

            start+=1
            end +=1
        
        return ret