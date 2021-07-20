# https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    # Be careful of the indexing since dp grid has additional row and column
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_side = max(max_side, dp[r+1][c+1])

        return max_side * max_side


# Time complexity : O(mn). Single pass - row x col (m=row; n=col)
# Space complexity: O(mn). Additional space for dp grid(don't need to worry about additional 1 row and col).

# Space can be optimized as we don't need to keep the whole dp grid as we progress down the rows in matrix.


# ----------------------------------------------------------------
# https://leetcode.com/problems/maximal-square/solution/
# Brute-Force:
# Time complexity :  O((mn)^2). In worst case, we need to traverse the complete matrix for every 1.
# Space complexity : O(1). No extra space is used.


# Better DP:
# Time complexity :  O(mn). Single pass.
# Space complexity : O(n). Another array which stores elements in a row is used for dp.
