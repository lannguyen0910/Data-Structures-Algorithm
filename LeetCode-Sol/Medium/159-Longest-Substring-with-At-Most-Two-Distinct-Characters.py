class Solution:
    def longest_substr_dist_char_count_2(self, string: str) -> int:
        count = collections.defaultdict(int)
        n = len(s)
        start = end = longest = 0
        # 2 pointers / sliding window
        while end < n:
            count[s[end]] += 1
            end +=1

            while len(count)>2:
                c = s[start]
                count[c] -= 1

                if count[c] == 0:
                    count.pop(c)

                start += 1

            longest = max(longest, end-start)
        
        return longest
            
    # Time complexity: O(n)
        
    '''
    NOTE: This problem is for Premium only. I didn't have access at the time of this file created. This soln belongs to CodePath.
    '''