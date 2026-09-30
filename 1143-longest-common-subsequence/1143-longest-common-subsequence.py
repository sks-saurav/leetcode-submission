class Solution:
    def longestCommonSubsequence(self, T1: str, T2: str) -> int:
        m, n = len(T1), len(T2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if T1[i-1] == T2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]