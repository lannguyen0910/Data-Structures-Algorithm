class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        
        def helper(x: int, y: int, s: str) -> bool:
            if not s:
                return True
            
            # check inbound
            if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0: # if not (0<=x<len(board[0])) or not (0<=y<len(board))
                return False
                        
            # check value
            if board[y][x] != s[0] or (y,x) in visited:
                return False
            
            visited.add((y, x))
            
            # return True if 1 of results is True -> also all()
            return any(helper(x2, y2, s[1:]) for (x2, y2) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)])


        return any(helper(x, y, word)
                    for x in range (0, len(board[0]))
                    for y in range (0, len(board)))

# CodePath week6 session2 lecture (modified to visit just once)

# STILL NOT SUCCESSFULLY SUBMITTED