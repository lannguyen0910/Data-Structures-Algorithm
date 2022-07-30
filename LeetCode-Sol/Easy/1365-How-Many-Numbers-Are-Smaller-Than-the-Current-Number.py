class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        # init
        max_val = max(nums)
        arr = [0]*(max_val+1)
        for i in nums:
            arr[i] += 1
        
        # counting
        count = 0
        arr_2 = [0]*(max_val+1)
        for i in range(max_val+1):
            if arr[i]!=0:
                arr_2[i] = count
                count += arr[i]

        ret = [arr_2[i] for i in nums]
        return ret

    # O(n)