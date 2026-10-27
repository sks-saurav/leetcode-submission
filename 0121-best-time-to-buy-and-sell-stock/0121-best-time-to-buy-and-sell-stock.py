class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bestBuyDay = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            profit = max(profit, prices[i]-bestBuyDay)
            bestBuyDay = min(bestBuyDay, prices[i])

        return profit
