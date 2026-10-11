class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        if firstLen+secondLen > len(nums):
            return 0

        n = len(nums)
        psum = [0] * (n+1)
        for i in range(n):
            psum[i+1] = nums[i] + psum[i]

        def s(x, y):
            if x < 0 or y >= n:
                return float('-inf')
            return psum[y+1]-psum[x]

        ans = 0
        # first, second
        for i in range(n):
            for j in range(i+firstLen, n):
                a = s(i, i+firstLen-1)
                b = s(j, j+secondLen-1)
                ans = max(ans, a+b)

        # second, first
        for i in range(n):
            for j in range(i+secondLen, n):
                a = s(i, i+secondLen-1)
                b = s(j, j+firstLen-1)
                ans = max(ans, a+b)

        return ans

        