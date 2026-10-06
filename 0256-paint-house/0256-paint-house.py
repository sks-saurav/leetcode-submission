class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        MAX = float('inf')
        dp = [[MAX] * 3 for _ in range(n)]
        dp[0] = costs[0]

        for i in range(1, n):
            for j in range(3):
                p1, p2 = (j+1)%3, (j+2)%3
                dp[i][j] = costs[i][j] + min(dp[i-1][p1], dp[i-1][p2])

        return min(dp[n-1])