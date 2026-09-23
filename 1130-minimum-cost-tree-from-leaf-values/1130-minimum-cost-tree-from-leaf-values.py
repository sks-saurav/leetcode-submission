class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        # Precompute
        n = len(arr)
        maxs = [[0] * n for _ in range(n)]
        for i in range(n):
            maxs[i][i] = arr[i]
            for j in range(i+1, n):
                maxs[i][j] = max(maxs[i][j-1], arr[j])

        # MCM DP Iterative
        dp = [[0]*n for _ in range(n)]
        for l in range(1, n):
            for i in range(0, n-l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = maxs[i][k] * maxs[k+1][j]
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + cost)

        return dp[0][n-1]
