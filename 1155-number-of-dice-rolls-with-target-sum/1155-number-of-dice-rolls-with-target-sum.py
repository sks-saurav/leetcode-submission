class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # ways (target, f, d)
        dp = [[0] * (n+1) for _ in range(target+1)]
        MOD = int(1e9) + 7

        dp[0][0] = 1

        for d in range(1, n+1):
            for val in range(1, target+1):
                for f in range(1, k+1):
                    if val >= f:
                        ways = dp[val-f][d-1]
                        dp[val][d] = (dp[val][d] + ways) % MOD

        return dp[target][n]