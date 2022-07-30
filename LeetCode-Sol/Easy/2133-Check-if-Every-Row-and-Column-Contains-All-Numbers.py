class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        if not matrix:
            return False
        
        n = len(matrix)
        
        # check row
        for row in range(n):
            seen = set()
            for col in range(n):
                val = matrix[row][col]
                if val in seen or val<=0 or val>n:
                    return False
                else:
                    seen.add(val)
        
        # check col
        for col in range(n):
            seen = set()
            for row in range(n):
                val = matrix[row][col]
                if val in seen or val<=0 or val>n:
                    return False
                else:
                    seen.add(val)
        
        return True
        