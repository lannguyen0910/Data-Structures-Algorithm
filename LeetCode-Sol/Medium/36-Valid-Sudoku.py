class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        
        row_num = len(board)
        col_num = len(board[0])
        
        # check rows:
        for row in range(row_num):
            seen = set([])
            for col in range(col_num):
                val = board[row][col]
                if val.isdigit() and val in seen:
                    return False
                else:
                    seen.add(val)
        
        # check cols:
        for col in range(col_num):
            seen = set([])
            for row in range(row_num):
                val = board[row][col]
                if val.isdigit() and val in seen:
                    return False
                else:
                    seen.add(val)
        
        # check 3x3 matrix
        # loop every 3x3 matrix
        for row in range(0, row_num, 3):
            for col in range(0, col_num, 3):
                # loop every ele in 3x3 matrix
                seen = set([])
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        val = board[i][j]
                        if val.isdigit() and val in seen:
                            return False
                        else:
                            seen.add(val)
        
        return True