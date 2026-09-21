class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        '''
        Smashing stones repeatedly is equivalent to assigning each stone a sign (+ or -)
        total_sum = s_1 + s_2
        Delta = s_1 - s_2 = (total_sum - s_2) - s_2 = total_sum - 2*s_2

        To minimize Delta >= 0, we must maximize s_2 under the constraint s_2 le lf floor total_sum / 2. This reduces the problem to the standard 0/1 Knapsack Problem.
        '''
        totalSum = sum(stones)
        w = totalSum // 2
        n = len(stones)

        # dp = [0] * (w + 1)
        # for i in range(n):
        #     val = stones[i]
        #     for j in range(w, val-1, -1):
        #         dp[j] = max(dp[j], val + dp[j-val])

        # return  totalSum - 2*dp[w]

        # dp[i][j] -> max wt of stone can be picked using till ith stone with bag capacity w
        dp = [[0]*(w+1) for _ in range(n+1)]

        for i in range(1, n+1):
            val = stones[i-1]
            for j in range(1, w+1):
                if j-val >= 0:
                    dp[i][j] = max(val + dp[i-1][j-val], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        return totalSum - 2*dp[n][w]




