class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        profit1 = [0] * n

        lowestPrice = prices[0]
        for i in range(1, n):
            profit1[i] = max(profit1[i-1], prices[i]-lowestPrice)
            lowestPrice = min(lowestPrice, prices[i])

        ans = max(profit1)
        highestPrice = prices[n-1]
        profit2 = 0
        for i in range(n-2, 0, -1):
            currProfit = profit1[i-1] + (highestPrice - prices[i])
            profit2 = max(currProfit, profit2)
            highestPrice = max(highestPrice, prices[i])

        return max(ans, profit2)
        