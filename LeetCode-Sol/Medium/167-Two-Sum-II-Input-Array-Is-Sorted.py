class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict = {}
        idx = 1
        for val in numbers:
            remain = target - val
            if remain in list(my_dict.keys()):
                small = min(my_dict.get(remain), idx)
                big = max(my_dict.get(remain), idx)
                return list([small, big])
            
            my_dict[val] = idx
            idx+=1

