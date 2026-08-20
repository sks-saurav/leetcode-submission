class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def dig_sum(dig):
            val = 0
            while dig > 0:
                val += (dig % 10)
                dig = dig // 10
            return val

        arr = [(dig_sum(dig), dig) for dig in nums]
        arr.sort()
        idx_map = {arr[i][1] : i for i in range(len(arr))}

        swap = 0
        for i in range(len(arr)):
            d_idx = idx_map[nums[i]]
            j = i
            while j != d_idx:
                swap += 1
                nums[j], nums[d_idx] = nums[d_idx], nums[j]
                d_idx = idx_map[nums[j]]


        return swap