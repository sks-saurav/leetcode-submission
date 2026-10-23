class Solution:
    def sortPermutation(self, nums):
        MAX = (1 << 30) - 1
        mask = MAX 
        
        for i, val in enumerate(nums):
            if val != i:
                mask &= val
                
        return 0 if mask == MAX else mask 