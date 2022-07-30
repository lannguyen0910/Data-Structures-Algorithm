class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for idx in range(len(s)):
            tmp = s[idx:] + s[:idx]
            if tmp == goal:
                return True
        return False