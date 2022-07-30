class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        col = len(matrix[0])
        row = len(matrix)
        
        if not matrix:
            return False
        if col < 2 or row < 2:
            return True
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True
        