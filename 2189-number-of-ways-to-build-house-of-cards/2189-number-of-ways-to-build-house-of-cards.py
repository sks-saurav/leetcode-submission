class Solution:
    def houseOfCards(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(2, n+1, 3):
            for j in range(n, i-1, -1):
                dp[j] += dp[j-i]
                
        return dp[n]