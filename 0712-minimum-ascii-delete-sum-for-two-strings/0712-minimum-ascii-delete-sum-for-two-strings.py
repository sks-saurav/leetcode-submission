class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        ## MEMO
        # @cache
        # def helper(i1, i2):
        #     if i1 < 0:
        #         return sum(ord(c) for c in s2[:i2+1])

        #     if i2 < 0:
        #         return sum(ord(c) for c in s1[:i1+1])

        #     cost1 = float('inf')
        #     if s1[i1] == s2[i2]:
        #         cost1 = helper(i1-1, i2-1)

        #     cost2 = helper(i1-1, i2) + ord(s1[i1])
        #     cost3 = helper(i1, i2-1) + ord(s2[i2])
        #     return min(cost1, cost2, cost3)

        # return helper(len(s1)-1, len(s2)-1)

        ## Bottom up
        n1, n2 = len(s1), len(s2)
        dp = [[float('inf')]*(n2+1) for _ in range(n1+1)]

        # fill base case
        dp[0][0] = 0
        for i in range(n1):
            dp[i+1][0] = ord(s1[i]) + dp[i][0]

        for i in range(n2):
            dp[0][i+1] = ord(s2[i]) + dp[0][i]


        for i in range(n1):
            for j in range(n2):
                dp[i+1][j+1] = min(dp[i][j+1] + ord(s1[i]), dp[i+1][j] + ord(s2[j]))
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j+1])

        return dp[n1][n2]







            
                