# PREMIUM
class Solution:
    def isThereAPath(self, grid: list[list[int]]) -> bool:
        row, col = len(grid), len(grid[0])
        
        # OPTIMIZATION: A path from (0,0) to (m-1,n-1) takes exactly (row + col - 1) steps.
        # If the total number of steps is odd, it's mathematically impossible to have an equal number of 0s and 1s.
        if (row + col - 1) % 2 != 0:
            return False

        def dfs(x, y, parity):
            if x >= row or y >= col:
                return False
            
            d = 1 if grid[x][y] == 1 else -1
            current_parity = parity + d
            
            if x == row - 1 and y == col - 1:
                return current_parity == 0
            
            state = (x, y, current_parity)
            if state in memo: 
                return memo[state]

            ans = dfs(x + 1, y, current_parity) or dfs(x, y + 1, current_parity)

            memo[state] = ans
            return ans

        memo = {}
        return dfs(0, 0, 0)