# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        row = [-1]*n
        matrix = []
        for i in range(m):
            matrix.append(row.copy())
        
        # right, down, left, 
        go_row = [0, 1, 0, -1]
        go_col = [1, 0, -1, 0]

        direction = 0
        curr_row = curr_col = 0
        
        currNode = head
        while currNode:
            matrix[curr_row][curr_col] = currNode.val
            # update currNode
            currNode = currNode.next
            # check new position
            new_row = curr_row + go_row[direction]
            new_col = curr_col + go_col[direction]
            # check inbound and not visit
            if 0<=new_row and new_row<m and 0<=new_col and new_col<n and matrix[new_row][new_col]==-1:
                curr_row, curr_col = new_row, new_col
            else:
                direction = (direction+1)%4
                curr_row = curr_row + go_row[direction]
                curr_col = curr_col + go_col[direction]
            
        return matrix

# weekly contest 300