# class Solution:
#     def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
#         n = len(nums)
#         # Precompute k-length subarray sums
#         ksum = [sum(nums[:k])]
#         for i in range(k, n):
#             ksum.append(ksum[-1] - nums[i - k] + nums[i])

#         m = len(ksum)
#         memo = [[-1] * 4 for _ in range(m)]

#         def helper(idx: int, taken: int) -> int:
#             if taken == 3:
#                 return 0
#             if idx >= m:
#                 return float('-inf')
#             if memo[idx][taken] != -1:
#                 return memo[idx][taken]

#             take = ksum[idx] + helper(idx + k, taken + 1)
#             leave = helper(idx + 1, taken)

#             memo[idx][taken] = max(take, leave)
#             return memo[idx][taken]

#         helper(0, 0)

#         # Reconstruct path
#         result = []
#         idx = 0
#         taken = 0

#         while idx < m and taken < 3:
#             # Optimal value if we choose to take index `idx`
#             next_take_val = helper(idx + k, taken + 1)
#             take_val = ksum[idx] + next_take_val

#             # If taking matches the memoized optimal value, choose it
#             if take_val == memo[idx][taken]:
#                 result.append(idx)
#                 idx += k
#                 taken += 1
#             else:
#                 idx += 1

#         return result

class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        
        # 1. Precompute window sums of length k
        ksum = [sum(nums[:k])]
        for i in range(k, n):
            ksum.append(ksum[-1] - nums[i - k] + nums[i])
        
        m = len(ksum)
        
        # 2. left[i]: starting index of the maximum window in ksum[0...i]
        # Using '>' preserves the smallest (leftmost) index on ties
        left = [0] * m
        best_left = 0
        for i in range(m):
            if ksum[i] > ksum[best_left]:
                best_left = i
            left[i] = best_left
            
        # 3. right[i]: starting index of the maximum window in ksum[i...m-1]
        # Using '>=' preserves the smallest (leftmost) index on ties
        right = [0] * m
        best_right = m - 1
        for i in range(m - 1, -1, -1):
            if ksum[i] >= ksum[best_right]:
                best_right = i
            right[i] = best_right
            
        # 4. Iterate over the middle window j
        # Middle window can start from k up to m - 1 - k
        max_total = -1
        ans = []
        for j in range(k, m - k):
            l = left[j - k]
            r = right[j + k]
            total = ksum[l] + ksum[j] + ksum[r]
            
            # Strictly greater ensures lexicographical preference for middle
            if total > max_total:
                max_total = total
                ans = [l, j, r]
                
        return ans