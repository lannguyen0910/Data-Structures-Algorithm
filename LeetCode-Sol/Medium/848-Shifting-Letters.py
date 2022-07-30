class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        if not s:
            return ''
        if not shifts:
            return s
        
        shift_val = [0] * len(s)
        shift_val[0] = sum(shifts)
        
        for i in range(1, len(s)):
            shift_val[i] = shift_val[i-1] - shifts[i-1]
        
        ret = []
        for i in range(len(s)):
            curr_val = ord(s[i]) - ord('a')
            val = shift_val[i] + curr_val
            # use this instead of ret = ret + str (init ret='') -> O(n) while list.append() is O(1)
            ret.append(chr(val%26 + ord('a')))
        
        
        return ''.join(ret)
    