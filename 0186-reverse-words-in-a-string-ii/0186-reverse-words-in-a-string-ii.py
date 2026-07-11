# PREMIUM
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if not s or len(s) == 0:
            return s

        def reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        
        reverse(0, len(s)-1)
        i, j = 0, 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != ' ':
                j += 1

            reverse(i, j-1)
            i = j+1



        