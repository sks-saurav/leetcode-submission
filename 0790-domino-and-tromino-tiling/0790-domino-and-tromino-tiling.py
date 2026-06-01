class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        # Base cases
        if n <= 2:
            return n
        if n == 3:
            return 5
            
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        
        # Apply the simplified recurrence relation
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
            
        return dp[n]