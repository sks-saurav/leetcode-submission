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
        dp = [0] * (w + 1)
        n = len(stones)

        for i in range(n):
            val = stones[i]
            for j in range(w, val-1, -1):
                dp[j] = max(dp[j], val + dp[j-val])

        return  totalSum - 2*dp[w]




