class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]

        for l in range(2, n + 1):
            for st in range(1, n - l + 2):
                end = st + l - 1
                dp[st][end] = float('inf')

                # Try guessing every number 'k' in the current range [st, end]
                for k in range(st, end + 1):
                    # We pay 'k', plus the worst-case scenario (max) of the two remaining halves
                    left_dp = dp[st][k-1] if k != 0 else 0
                    right_dp = dp[k + 1][end] if k != end else 0
                    cost = k + max(left_dp, right_dp)
                    
                    # We want the guess that gives us the lowest possible worst-case cost (min)
                    dp[st][end] = min(dp[st][end], cost)

        return dp[1][n]

# class Solution:
#     def getMoneyAmount(self, n: int) -> int:
#         dp = {}

#         def helper(st, end):
#             if st >= end:
#                 return 0
            
#             key = (st, end)
#             if key in dp: return dp[key]
            
#             ans = float('inf')

#             for k in range(st, end+1):
#                 cost = k + max(helper(st, k-1), helper(k+1, end))
#                 ans = min(cost, ans)

#             dp[key] = ans
#             return ans

#         res = helper(1, n)
#         return res