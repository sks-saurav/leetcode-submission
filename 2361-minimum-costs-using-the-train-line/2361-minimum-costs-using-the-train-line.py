class Solution:
    def minimumCosts(self, regular: list[int], express: list[int], expressCost: int) -> list[int]:
        
        n = len(regular)
        dp = [[float('inf')] * 2 for _ in range(n+1)]
        dp[0][0] = 0
        dp[0][1] = expressCost

        for i in range(1, n+1):
            dp[i][0] = min(
                dp[i-1][0] + regular[i-1],
                dp[i-1][1] + regular[i-1]
            )
            dp[i][1] = min(
                dp[i-1][0] + express[i-1] + expressCost,
                dp[i-1][1] + express[i-1] 
            )

        ans = []
        for i in range(1, n+1):
            ans.append(min(dp[i][0], dp[i][1]))

        return ans
