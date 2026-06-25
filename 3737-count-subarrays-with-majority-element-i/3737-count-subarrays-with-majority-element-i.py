class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        def eligible_count(window_len):
            count_in_window = 0
            result = 0

            for i in range(len(nums)):
                count_in_window += (nums[i] == target)

                if i >= window_len:
                    count_in_window -= (nums[i - window_len] == target)

                if i >= window_len - 1:
                    if 2 * count_in_window > window_len:
                        result += 1

            return result
            

        ans = 0        
        for l in range(1, len(nums)+1):
            ans += eligible_count(l)

        return ans

