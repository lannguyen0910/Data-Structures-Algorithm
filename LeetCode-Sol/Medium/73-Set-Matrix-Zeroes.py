class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set, col_set = set(), set()
        rows, cols = len(matrix), len(matrix[0])

        # get 0 locations
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_set.add(row)
                    col_set.add(col)

        # Assign 0 to recored rows/cols
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in row_set or col in col_set:
                    matrix[row][col]=0