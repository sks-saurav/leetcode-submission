class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = int(1e9) + 7
        
        # You can reach at most steps // 2 and still return to 0
        max_pos = min(arrLen, steps // 2 + 1)
        
        # dp[j] = number of ways to be at index j
        # Base case: 0 steps taken, we are at index 0 in 1 way
        dp = [0] * max_pos
        dp[0] = 1
        
        for _ in range(steps):
            next_dp = [0] * max_pos
            for j in range(max_pos):
                ways = dp[j] # Stay

                if j > 0: # MOVE left
                    ways = (ways + dp[j - 1]) % MOD
                    
                if j + 1 < max_pos: # move right
                    ways = (ways + dp[j + 1]) % MOD
                
                next_dp[j] = ways
            dp = next_dp
            
        return dp[0]

# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#         MOD = int(1e9) + 7

#         @cache
#         def helper(idx, step):
#             if idx < 0 or idx >= arrLen:
#                 return 0

#             if step == 0:
#                 return 1 if idx == 0 else 0

#             ans = 0
#             ans = (ans + helper(idx-1, step-1)) % MOD
#             ans = (ans + helper(idx, step-1)) % MOD
#             ans = (ans + helper(idx+1, step-1)) % MOD

#             return ans 

#         return helper(0, steps)
