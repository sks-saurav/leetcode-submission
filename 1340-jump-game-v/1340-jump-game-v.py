class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        @cache
        def helper(idx):
            ans = 1
            i = idx+1
            while i < len(arr) and i <= idx+d and arr[idx] > arr[i]:
                ans = max(ans, 1 + helper(i))
                i += 1
            
            i = idx-1
            while i >= 0 and i >= idx-d and arr[idx] > arr[i]:
                ans = max(ans, 1+helper(i))
                i -= 1

            return ans

        result = 0
        for i in range(len(arr)):
            result = max(result, helper(i))

        return result