# PREMIUM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        rn = [0] * n
        rn[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] == 1:
                rn[i] = 1 + rn[i+1]

        ans = max(rn)
        left = 0
        for i in range(0, n):
            if nums[i] == 0:
                tans = 1
                if i != 0: tans += left
                if i != n-1: tans += rn[i+1]
                ans = max(ans, tans)
                left = 0
            else:
                left += 1
            
        return ans

