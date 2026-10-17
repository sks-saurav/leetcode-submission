class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        row, col = len(grid), len(grid[0])
        
        left = [[0] * col for _ in range(row)]
        right = [[0] * col for _ in range(row)]
        up = [[0] * col for _ in range(row)]
        down = [[0] * col for _ in range(row)]
        
        # Left and Up passes
        for i in range(row):
            for j in range(col):
                if grid[i][j] != 'W':
                    is_enemy = 1 if grid[i][j] == 'E' else 0
                    left[i][j] = is_enemy + (left[i][j-1] if j > 0 else 0)
                    up[i][j] = is_enemy + (up[i-1][j] if i > 0 else 0)
        
        # Right and Down passes
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if grid[i][j] != 'W':
                    is_enemy = 1 if grid[i][j] == 'E' else 0
                    right[i][j] = is_enemy + (right[i][j+1] if j < col - 1 else 0)
                    down[i][j] = is_enemy + (down[i+1][j] if i < row - 1 else 0)
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    tans = left[i][j] + right[i][j] + up[i][j] + down[i][j]
                    ans = max(ans, tans)
                    
        return ans