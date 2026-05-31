class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Precompute the MEX of every suffix
        # suffix_mex[i] will store the MEX of nums[i...n-1]
        suffix_mex = [0] * n
        seen = set()
        current_mex = 0
        
        # Traverse from right to left to build suffix_mex
        for i in range(n - 1, -1, -1):
            seen.add(nums[i])
            # Increment current_mex while it exists in our seen set
            while current_mex in seen:
                current_mex += 1
            suffix_mex[i] = current_mex
            
        result = []
        i = 0
        
        # Step 2: Greedily build the result array from left to right
        while i < n:
            # Our target is the absolute maximum MEX the remaining array can achieve
            target_mex = suffix_mex[i]
            
            prefix_seen = set()
            prefix_mex = 0
            
            # Expand the current slice until its MEX hits the target
            while i < n:
                prefix_seen.add(nums[i])
                
                # Update the MEX of our current slice
                while prefix_mex in prefix_seen:
                    prefix_mex += 1
                
                # If we hit our target, make the cut immediately!
                if prefix_mex == target_mex:
                    result.append(target_mex)
                    i += 1  # Move to the next element for the start of the next slice
                    break
                    
                i += 1
                
        return result    