class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        # Prefix sum array: psum[k] is sum of nums[0..k-1]
        psum = [0] * (n + 1)
        for i in range(n):
            psum[i + 1] = psum[i] + nums[i]

        max_first = 0
        max_second = 0
        ans = 0

        # Case 1 & Case 2 evaluated simultaneously in one pass
        for i in range(firstLen + secondLen, n + 1):
            # Case 1: firstLen window before secondLen window
            # firstLen window ends at i - secondLen
            first_sum = psum[i - secondLen] - psum[i - secondLen - firstLen]
            max_first = max(max_first, first_sum)

            # secondLen window ends at i
            second_sum = psum[i] - psum[i - secondLen]

            # Case 2: secondLen window before firstLen window
            # secondLen window ends at i - firstLen
            second_sum_prev = psum[i - firstLen] - psum[i - firstLen - secondLen]
            max_second = max(max_second, second_sum_prev)

            # firstLen window ends at i
            first_sum_curr = psum[i] - psum[i - firstLen]

            ans = max(ans, max_first + second_sum, max_second + first_sum_curr)

        return ans