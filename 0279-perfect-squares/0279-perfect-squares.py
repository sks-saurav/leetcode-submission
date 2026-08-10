class Solution:
    def numSquares(self, n: int) -> int:
        ## MEMOIZATION (memory limit error)
        # cand = []
        # i = 1

        # while i * i <= n:
        #     cand.append(i*i)
        #     i += 1
        # dp = {}

        # def square_count(idx, rem_n):
        #     if rem_n == 0: return 0
        #     if idx == len(cand): return float('inf')

        #     key = (idx, rem_n)
        #     if key in dp: return dp[key]

        #     ways = square_count(idx+1, rem_n)
        #     if cand[idx] <= rem_n:
        #         tways = square_count(idx, rem_n - cand[idx])
        #         ways = min(ways, 1 + tways)
            
        #     dp[key] = ways
        #     return ways

        # return square_count(0, n)

        ## TABULATION
        l = int(math.sqrt(n)) + 1
        dp = [[float('inf')] * (n+1) for _ in range(l)]
        
        # BASE CASE: It takes 0 squares to make a sum of 0
        for i in range(l):
            dp[i][0] = 0

        for i in range(1, l):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j]
                if i*i <= j:
                    dp[i][j] = min(dp[i][j], 1 + dp[i][j - i*i])

        return dp[-1][-1]
