class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        # dp[i][0]: Maximum profit on day i holding 0 shares (either did nothing or just sold).
        # dp[i][1]: Maximum profit on day i holding 1 share (either continued holding or just bought).

        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        # basecase : TODO
        dp[0][0] = 0
        dp[0][1] = -prices[0]


        for i in range(1, n):
            # Hold stock or buy new stock today
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])

            # Keep cash or sell today
            dp[i][0] = max(dp[i-1][1] + prices[i] - fee, dp[i-1][0])

        return dp[n-1][0]