class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        # dp[i][j][hold] profit ith day, completed j txn holding 0 or 1 stock
        
        n = len(prices)
        dp = [[[float('-inf')]*2 for _ in range(k+1)] for _ in range(n)]


        # base case
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]

        for i in range(1, n):
            for j in range(k+1):
                if j == 0:
                    dp[i][j][0] = dp[i-1][j][0]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1] + prices[i])
                
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j][0] - prices[i])

        ans = 0
        for j in range(k+1):
            ans = max(ans, dp[n-1][j][0])

        return ans
        