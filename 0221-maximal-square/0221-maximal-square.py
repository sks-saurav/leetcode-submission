class Solution:
    def maximalSquare(self, M: list[list[str]]) -> int:
        row, col = len(M), len(M[0])
        dp = [[0] * (col) for _ in range(row)]

        for i in range(row):
            dp[i][0] = 1 if M[i][0] == '1' else 0
        for j in range(col):
            dp[0][j] = 1 if M[0][j] == '1' else 0


        for i in range(1, row):
            for j in range(1, col):
                if M[i][j] == '0': continue
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])


        ans = 0
        for arr in dp:
            ans = max(ans, max(arr))

        return ans*ans
        
            