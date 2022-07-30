# https://leetcode.com/problems/trapping-rain-water/solution/
# bruteforce: O(n^2), O(1)
# DP: O(n), O(n)

# 2 pointers: O(n), O(1)
def trap(height):

    if len(height) <= 2:
        return 0

    ans = 0

    # using two pointers i and j on indices 1 and n-1
    i = 1
    j = len(height) - 1

    # initialising leftmax to the leftmost bar and rightmax to the rightmost bar
    lmax = height[0]
    rmax = height[-1]

    while i <= j:
        # check lmax and rmax for current i, j positions
        if height[i] > lmax:
            lmax = height[i]
        if height[j] > rmax:
            rmax = height[j]

        # fill water upto lmax level for index i and move i to the right
        if lmax <= rmax:
            ans += lmax - height[i]
            i += 1

        # fill water upto rmax level for index j and move j to the left
        else:
            ans += rmax - height[j]
            j -= 1

    return ans


print(trap([4, 2, 0, 3, 2, 5]))
