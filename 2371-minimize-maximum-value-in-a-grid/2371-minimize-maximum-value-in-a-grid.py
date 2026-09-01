# PREMIUM
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        nums = [(v, i, j) for i, r in enumerate(grid) for j, v in enumerate(r)]
        nums.sort()
        
        row_max = [0] * row
        col_max = [0] * col
        ans = [[0] * col for _ in range(row)]
        
        for _, i, j in nums:
            ans[i][j] = max(row_max[i], col_max[j]) + 1
            row_max[i] = col_max[j] = ans[i][j]
            
        return ans