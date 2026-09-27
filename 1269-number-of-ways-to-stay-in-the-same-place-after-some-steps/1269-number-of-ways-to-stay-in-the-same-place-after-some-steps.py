class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = int(1e9) + 7
        
        @cache
        def helper(idx, step):
            if idx < 0 or idx >= arrLen:
                return 0

            if step == 0:
                return 1 if idx == 0 else 0

            ans = 0
            ans = (ans + helper(idx-1, step-1)) % MOD
            ans = (ans + helper(idx, step-1)) % MOD
            ans = (ans + helper(idx+1, step-1)) % MOD

            return ans 

        return helper(0, steps)
