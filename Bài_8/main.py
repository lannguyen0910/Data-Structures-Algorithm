from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    ## APPROACH : BACKTRACKING ##
    ## TIME COMPLEXICITY : O(N!) ##
    ## SPACE COMPLEXICITY : O(N) ##

    puzzle = [["."*n] for i in range(n)]
    cols, diagonals, anti_diagonals, result = set(), set(), set(), []

    def place_queen(row, puzzle):

        if(row == n):
            result.append(puzzle[:])
            return

        for col in range(n):
            # GIST, we can uniquely identify diagonals and antidiagonals by row-col and row+col
            # check if collision at all directions
            if(col in cols or (row-col) in diagonals or (row + col) in anti_diagonals):
                continue
            print("row: ", row)
            print("Col: ", col)
            cols.add(col)
            diagonals.add(row - col)
            anti_diagonals.add(row + col)

            puzzle[row] = "." * (col) + "Q" + "." * (n-col-1)

            place_queen(row + 1, puzzle)

            # if all col not satisfy, remove the current row, go to next col
            cols.remove(col)
            diagonals.remove(row - col)
            anti_diagonals.remove(row + col)

            puzzle[row] = "." * n

    place_queen(0, puzzle)
    print("len: ", len(result))
    return result


print(solveNQueens(4))
