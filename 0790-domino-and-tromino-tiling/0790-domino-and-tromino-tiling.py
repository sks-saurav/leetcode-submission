class Solution:
    def numTilings(self, n):
        MOD = int(1e9) + 7
        if n <= 2:
            return n

        # F[k] ways of fully covering k width board
        # P[k] ways of partially covering k width board
        # f(k) = f(k-1) + f(k-2) * 2*p(k-1)
        # p(k) = p(k-1) + f(k-2)

        F = [0] * (n+1)
        P = [0] * (n+1)

        F[1] = 1
        F[2] = 2
        P[2] = 1

        for k in range(3, n+1):
            F[k] = (F[k-1] + F[k-2] + 2*P[k-1]) % MOD
            P[k] = (P[k-1] + F[k-2]) % MOD

        return F[n]
        
# eliminate P using above two equation to optimize
# result:  f(i) = 2*f(i-1) + f(i-3)
# class Solution:
#     def numTilings(self, n: int) -> int:
#         MOD = 10**9 + 7
        
#         # Base cases
#         if n <= 2:
#             return n
#         if n == 3:
#             return 5
            
#         dp = [0] * (n + 1)
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 5
        
#         # Apply the simplified recurrence relation
#         for i in range(4, n + 1):
#             dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD
            
#         return dp[n]