class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        def eligible_count(l):
            ele_count = 0
            i, j = 0, 0
            while i < l:
                if nums[i] == target:
                    ele_count += 1
                i += 1

            subarray_count = 1 if 2 * ele_count > l else 0
            while i < len(nums):
                if nums[i] == target:
                    ele_count += 1
                if nums[j] == target:
                    ele_count -= 1

                if 2 * ele_count > l:
                    subarray_count += 1
                i += 1
                j += 1
            
            return subarray_count
            

        ans = 0        
        for l in range(1, len(nums)+1):
            ans += eligible_count(l)

        return ans

