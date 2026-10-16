class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        # Precompute k-length subarray sums
        ksum = [sum(nums[:k])]
        for i in range(k, n):
            ksum.append(ksum[-1] - nums[i - k] + nums[i])

        m = len(ksum)
        memo = [[-1] * 4 for _ in range(m)]

        def helper(idx: int, taken: int) -> int:
            if taken == 3:
                return 0
            if idx >= m:
                return float('-inf')
            if memo[idx][taken] != -1:
                return memo[idx][taken]

            take = ksum[idx] + helper(idx + k, taken + 1)
            leave = helper(idx + 1, taken)

            memo[idx][taken] = max(take, leave)
            return memo[idx][taken]

        helper(0, 0)

        # Reconstruct path
        result = []
        idx = 0
        taken = 0

        while idx < m and taken < 3:
            # Optimal value if we choose to take index `idx`
            next_take_val = helper(idx + k, taken + 1)
            take_val = ksum[idx] + next_take_val

            # If taking matches the memoized optimal value, choose it
            if take_val == memo[idx][taken]:
                result.append(idx)
                idx += k
                taken += 1
            else:
                idx += 1

        return result