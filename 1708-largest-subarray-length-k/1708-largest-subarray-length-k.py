class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        m_ele = nums[0]

        for i in range(n-k+1):
            m_ele = max(m_ele, nums[i])

        for i in range(n-k+1):
            if nums[i] == m_ele:
                return nums[i:i+k]

        return []