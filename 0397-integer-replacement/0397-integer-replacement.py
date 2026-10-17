class Solution:
    def integerReplacement(self, n: int) -> int:
        @cache
        def helper(x):
            if x == 1:
                return 0

            if x%2 == 0:
                return helper(x//2) + 1

            else:
                return 1 + min(helper(x-1), helper(x+1))

            
        return helper(n)