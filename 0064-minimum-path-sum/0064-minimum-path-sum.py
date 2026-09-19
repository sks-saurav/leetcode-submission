class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[float('inf')] * col for _ in range(row)]
        dp[0][0] = grid[0][0]

        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, col):
            dp[0][j] = dp[0][j-1] + grid[0][j]


        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[row-1][col-1]