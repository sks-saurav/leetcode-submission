class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = list(triangle[n-1])

        for i in range(n-2, -1, -1):
            temp = list(triangle[i])
            for j in range(len(triangle[i])-1, -1, -1):
                temp[j] = triangle[i][j] + min(dp[j], dp[j+1])
            dp = temp

        return dp[0]