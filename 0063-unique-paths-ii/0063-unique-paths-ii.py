class Solution:
    def uniquePathsWithObstacles(self, G: list[list[int]]) -> int:
        row, col = len(G), len(G[0])
        dp = [[0]*col for _ in range(row)]


        for i in range(row):
            if G[i][0] == 1: break
            dp[i][0] = 1

        for j in range(col):
            if G[0][j] == 1: break
            dp[0][j] = 1


        for i in range(1, row):
            for j in range(1, col):
                if G[i][j] == 1: continue

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[row-1][col-1]


