class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = columnTitle[::-1]
        
        ret = 0
        for i in range(len(columnTitle)):
            ret += int(ord(columnTitle[i].lower()) - ord('a') +1) * int(math.pow(26, i))
    
        return ret
