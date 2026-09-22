# Bottom UP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        n = len(coins)

        # dp[i][j] -> number of coin required using first i type of coin to make amount j 
        dp = [[MAX] * (amount+1) for _ in range(n+1)]
        for i in range(n+1): # Base Case
            dp[i][0] = 0

        for i in range(1, n+1):
            val = coins[i-1]
            for j in range(1, amount+1):
                if j-val >= 0:
                    dp[i][j] = min(1 + dp[i][j-val], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        ans = dp[n][amount]
        return -1 if ans == float('inf') else ans

# OPTIMIZED bottom up
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         n = len(coins)
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0

#         for i in range(n):
#             val = coins[i]
#             for j in range(val, amount+1):
#                 dp[j] = min(dp[j], dp[j - val] + 1)

#         ans = dp[amount]
#         return -1 if ans == float('inf') else ans