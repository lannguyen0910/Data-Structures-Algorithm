from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                arr.pop()
                i += 2
            else:
                i += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
test = Solution()
test.duplicateZeros(arr)
