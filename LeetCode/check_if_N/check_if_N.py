from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = []
        for i, v in enumerate(arr):
            if v*2 in seen or float(v)/2 in seen:
                return True
            if v not in seen:
                seen.append(v)

        return False


arr = [3, 1, 7, 11]
test = Solution()
test.checkIfExist(arr)
