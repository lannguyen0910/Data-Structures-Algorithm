class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        if not operations:
            return 0
        
        add_val = operations.count('++X') + operations.count('X++')
        subtr_val = operations.count('--X') + operations.count('X--')
        
        return add_val - subtr_val
        