# NOTE: The same-day overlap case refers to whether you are allowed to sell your first stock and immediately buy your second stock on the exact same day i
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        # buy1: Balance after 1st buy (minimizing effective cost).
        # sell1: Balance after 1st sell (max profit from transaction 1).
        # buy2: Balance after 2nd buy (reinvesting sell1 profit).
        # sell2: Balance after 2nd sell (final maximum profit).
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)

        return sell2

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
        