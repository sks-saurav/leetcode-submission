class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_pivot():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return r
        
        def binary_search(st, end):
            while st < end:
                mid = (st + end) // 2
                if nums[mid] >= target:
                    end = mid
                else:
                    st = mid+1
                    
            return st if nums[st] == target else -1
        
        pvt = find_pivot()
        
        # Step 3: Search both halves 
        ans1 = binary_search(0, pvt - 1)
        ans2 = binary_search(pvt, len(nums) - 1)

        return ans1 if ans1 != -1 else ans2