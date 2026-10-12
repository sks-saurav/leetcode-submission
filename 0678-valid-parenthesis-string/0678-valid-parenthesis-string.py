class Solution:
  def checkValidString(self, s: str) -> bool:
    n = len(s)
    # dp[i][j]: after processing prefix of length i, is balance j possible?
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = True

    for i, ch in enumerate(s):
      for j in range(n):
        if not dp[i][j]:
          continue

        if ch == "(":
          dp[i + 1][j + 1] = True
        elif ch == ")":
          if j > 0:
            dp[i + 1][j - 1] = True
        else:  # ch == '*'
          # Treat as '('
          dp[i + 1][j + 1] = True
          # Treat as ''
          dp[i + 1][j] = True
          # Treat as ')'
          if j > 0:
            dp[i + 1][j - 1] = True

    return dp[n][0]


# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         @cache
#         def helper(idx, open):
#             if open < 0:
#                 return False

#             if idx == len(s):
#                 return open == 0

#             if s[idx] == '(':
#                 return helper(idx+1, open+1)

#             elif s[idx] == ')':
#                 return helper(idx+1, open-1)

#             return helper(idx+1, open+1) or helper(idx+1, open) or helper(idx+1, open-1)

#         return helper(0, 0)