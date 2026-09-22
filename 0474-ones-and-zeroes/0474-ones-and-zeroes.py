class Solution:
    def findMaxForm(self, strs, m, n): 
        l = len(strs)
        # dp[i][j][k] max subset len by utilizing atmost j 0s and k 1s
        dp = [[[0] * (n+1) for _ in range(m+1)] for _ in range(l+1)]

        for i in range(1, l+1):
            c0 = strs[i-1].count('0')
            c1 = strs[i-1].count('1')

            for j in range(0, m+1):
                for k in range(0, n+1):
                    # choose
                    if j-c0 >= 0 and k-c1 >= 0:
                        dp[i][j][k] = max(
                            1 + dp[i-1][j-c0][k-c1],
                            dp[i-1][j][k]
                        )
                    # dont choose
                    else:
                        dp[i][j][k] = dp[i-1][j][k]

        return dp[l][m][n]



# class Solution:
#     def findMaxForm(self, strs, m, n):
#         """
#         Solves the 2D 0/1 Knapsack problem for subsets of binary strings.
#         """
#         # dp[i][j] stores the maximum subset size using at most i 0's and j 1's
#         dp = [[0] * (n + 1) for _ in range(m + 1)]
        
#         for s in strs:
#             zeros = s.count('0')
#             ones = s.count('1')
            
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
                    
#         return dp[m][n]