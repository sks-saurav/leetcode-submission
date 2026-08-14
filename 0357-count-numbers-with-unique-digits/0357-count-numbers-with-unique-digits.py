class Solution:
    """Mathematical Recursive Solution"""
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def dp(i):
            if i == 0:
                return 1
            if i == 1:
                return 9
            return (10 - (i - 1)) * dp(i - 1)

        total = 0
        for j in range(n + 1):
            total += dp(j)
        return total