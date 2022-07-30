class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        ptr = 0
        max_sub = 0
        
        for i in range(len(s)):
            c = s[i]
            
            if c in visited.keys():
                ptr = max(ptr, visited.get(c)+1)
            
            visited[c] = i
            max_sub = max(max_sub, i - ptr +1)
        return max_sub