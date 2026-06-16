# # Memoization DP
# class Solution:
#     def palindromePartition(self, s: str, k: int) -> int:
#         @cache
#         def count_change(st, end):
#             count = 0
#             while st < end:
#                 if s[st] != s[end]:
#                     count += 1
#                 st += 1
#                 end -= 1
#             return count

#         @cache
#         def helper(st, rk):
#             if rk == 1:
#                 return count_change(st, len(s)-1)

#             ans = len(s) - st
#             for end in range(st, len(s)-rk+1):
#                 change = count_change(st, end)
#                 ans = min(ans, change + helper(end+1, rk-1))

#             return ans

#         return helper(0, k)

## Bottom Up DP
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i+1][j-1] + (1 if s[i] != s[j] else 0)

        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        
        for i in range(n):
            dp[i][1] = cost[0][i]
            
        for j in range(2, k + 1):          # For each number of partitions from 2 to k
            for i in range(j - 1, n):      # End index of the current prefix
                for m in range(j - 2, i):
                    dp[i][j] = min(dp[i][j], dp[m][j-1] + cost[m+1][i])
                    
        return dp[n-1][k]