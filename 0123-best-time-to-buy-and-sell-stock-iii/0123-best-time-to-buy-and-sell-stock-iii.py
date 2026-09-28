class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        K = 2  # At most 2 transactions
        
        # dp[i][j][hold]: max profit on day i with j completed transactions
        # hold: 0 = no stock, 1 = holding 1 stock
        dp = [[[float('-inf')] * 2 for _ in range(K + 1)] for _ in range(n)]
        
        # Base cases on day 0
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        
        for i in range(1, n):
            for j in range(K + 1):
                # State 0: Not holding stock
                dp[i][j][0] = dp[i-1][j][0]
                if j > 0:  # Selling completes transaction j
                    dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1] + prices[i])
                
                # State 1: Holding stock
                dp[i][j][1] = dp[i-1][j][1]
                dp[i][j][1] = max(dp[i][j][1], dp[i-1][j][0] - prices[i])
        
        # The result is the max profit holding 0 stock across all valid transaction counts
        return max(dp[n-1][j][0] for j in range(K + 1))

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         n = len(prices)
#         profit1 = [0] * n

#         lowestPrice = prices[0]
#         for i in range(1, n):
#             profit1[i] = max(profit1[i-1], prices[i]-lowestPrice)
#             lowestPrice = min(lowestPrice, prices[i])

#         ans = max(profit1)
#         highestPrice = prices[n-1]
#         profit2 = 0
#         for i in range(n-2, 0, -1):
#             currProfit = profit1[i] + (highestPrice - prices[i])
#             profit2 = max(currProfit, profit2)
#             highestPrice = max(highestPrice, prices[i])

#         return max(ans, profit2)
        