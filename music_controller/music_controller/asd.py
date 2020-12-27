from functools import lru_cache
class Solution:
    def solve(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        
        @lru_cache(None)
        def dp(r, c):
            if r >= rows:
                return 0
            
            if c >= cols:
                return 0
                
            
            current = matrix[r][c]
            
            output1 = dp(r + 1, c) + current
            output2 = dp(r, c + 1) + current
            
            
            return max(output1, output2)
        
        return dp(0,0)
 