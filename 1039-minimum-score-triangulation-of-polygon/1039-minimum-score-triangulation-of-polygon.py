class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for l in range(3, n+1):
            for i in range(0, n-l+1):
                j = i+l-1
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    cost = values[i] * values[j] * values[k]
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cost)

        return dp[0][n-1]