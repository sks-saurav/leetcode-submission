# Iterative DP
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = piles[i]


        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i+l-1

                left = piles[i] - dp[i+1][j]
                right = piles[j] - dp[i][j-1]
                dp[i][j] = max(left, right)

        return dp[n-1][n-1] > 0



# Recursive DP
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
        
#         def game_dp(st, end):
#             if st == end:
#                 return piles[st]
#             state = (st, end)
#             if state in dp: return dp[state]

#             left = piles[st] - game_dp(st+1, end)
#             right = piles[end] - game_dp(st, end-1)

#             ans = max(left, right)
#             dp[state] = ans
#             return ans

#         dp = {}
#         return game_dp(0, len(piles)-1) > 0