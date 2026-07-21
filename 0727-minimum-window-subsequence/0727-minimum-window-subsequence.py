class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        min_len = float('inf')
        start_idx = -1
        
        i = 0
        while i < len(s1):
            # 1. Forward pass: find a valid window that contains s2
            j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] == s2[j]:
                    j += 1
                i += 1
            
            # If we reached the end of s1 without fully matching s2, we are done
            if j < len(s2):
                break
            
            # 2. Reverse pass: optimize the start position of this window
            end = i
            i -= 1
            j -= 1
            while j >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1
            
            # After the loop, i is one step before the optimal start
            start = i + 1
            
            # 3. Update the minimum window if this one is smaller
            if end - start < min_len:
                min_len = end - start
                start_idx = start
            
            # 4. Advance i to search for the next window
            # We must resume searching right after the start of our current valid window
            i = start + 1
            
        if start_idx == -1:
            return ""
            
        return s1[start_idx : start_idx + min_len]