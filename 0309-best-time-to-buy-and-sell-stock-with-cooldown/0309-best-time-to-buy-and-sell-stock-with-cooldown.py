class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
            
        # dp[i][0] -> max profit on day i holding 0 stock
        # dp[i][1] -> max profit on day i holding 1 stock
        dp = [[0] * 2 for _ in range(n)]

        # Base case: Day 0
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        # Base case: Day 1
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], -prices[1])

        for i in range(1, n):
            # Hold stock or buy new stock today
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

            # Keep cash or sell today
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])

        return dp[n - 1][0]
        