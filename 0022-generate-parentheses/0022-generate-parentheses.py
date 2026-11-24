from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current: str, open_count: int, close_count: int):
            # Base case: valid combination is complete
            if len(current) == 2 * n:
                res.append(current)
                return
            
            # Rule 1: We can add '(' if we haven't used all n opening parentheses
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
                
            # Rule 2: We can add ')' only if it won't exceed the number of '('
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res