class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''  
        sum(P) - sum(N) = target
        sum(P) + sum(N) = totalSum
        sum(P) = (target + totalSum) / 2

        Peduced to finding the number of ways to form subset with the sum = (target + totalSum) / 2
        '''
        totalSum = sum(nums)
        if abs(target) > totalSum or (target+totalSum) % 2 != 0:
            return 0

        S = (target+totalSum)//2
        dp = [0] * (S+1)
        n = len(nums)
        dp[0] = 1

        for i in range(n):
            for j in range(S, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        
        return dp[S]
     



        