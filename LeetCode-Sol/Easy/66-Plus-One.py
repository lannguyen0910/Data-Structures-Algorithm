class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits)==0:
            return None
        
        arr = digits.copy()[::-1]
        carry = 0
        
        val = arr[0]+1
        carry = val // 10
        add = val % 10
        arr[0] = add
        
        for i in range(1, len(arr)):
            val = arr[i]+carry
            carry = val // 10
            add = val % 10
            arr[i] = add
        
        if carry>0:
            arr.append(carry)
        
        return arr[::-1]