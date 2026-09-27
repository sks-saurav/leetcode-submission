"""
1. If lis[i] < lis[j] + 1 meaning we found a longer sequence and lis[i] need to be updated, then cnt[i] need to be updated to cnt[j]
2. If lis[i] == lis[j] + 1 meaning lis[j] + 1 is one way to reach longest increasing sequence to i, so simple increment by cnt[j] like this cnt[i] = cnt[i] + cnt[j]
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        lis = [1 for _ in range(n)]
        count = [1 for _ in range(n)]

        ans = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if lis[i] == lis[j]+1:
                        count[i] += count[j]
                    elif lis[i] < lis[j]+1:
                        count[i] = count[j]
                    lis[i] = max(lis[i], lis[j]+1)
            ans = max(ans, lis[i])
        res = 0
        for i in range(n):
            if lis[i] == ans:
                res += count[i]

        return res