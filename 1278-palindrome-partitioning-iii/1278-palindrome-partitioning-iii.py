class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def count_change(st, end):
            count = 0
            while st < end:
                if s[st] != s[end]:
                    count += 1
                st += 1
                end -= 1
            return count

        @cache
        def helper(st, rk):
            if rk == 1:
                return count_change(st, len(s)-1)

            ans = len(s) - st
            for end in range(st, len(s)-rk+1):
                change = count_change(st, end)
                ans = min(ans, change + helper(end+1, rk-1))

            return ans

        return helper(0, k)