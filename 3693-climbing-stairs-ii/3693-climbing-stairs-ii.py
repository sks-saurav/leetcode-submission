class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(n):
            for j in range(1, 4):
                if i+j <= n:
                    nxtIdx = i+j
                    newCost = dp[i] + (j*j) + costs[nxtIdx-1]
                    dp[nxtIdx] = min(dp[nxtIdx], newCost) 


        return dp[n]
        