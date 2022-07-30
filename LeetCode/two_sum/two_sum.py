# one_pass
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for id, first in enumerate(nums):
            second = target - first
            if second in res:
                return [res[second], id]
            res[first] = id

        return []


# naive two-loop

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)

        return res


nums = [2, 7, 11, 15]
target = 9
test = Solution()
test.twoSum(nums, target)
