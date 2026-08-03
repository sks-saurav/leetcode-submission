class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = list(nums)
        arr.sort()
        i, j, k = 0, 0, len(nums)-1
        while j < k:
            nums[i] = arr[j]
            i += 1
            nums[i] = arr[k]
            i += 1
            j += 1
            k -= 1

        if j == k:
            nums[i] = arr[j]

