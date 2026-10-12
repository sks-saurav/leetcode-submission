class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def helper(idx, open):
            if open < 0:
                return False

            if idx == len(s):
                return open == 0

            if s[idx] == '(':
                return helper(idx+1, open+1)

            elif s[idx] == ')':
                return helper(idx+1, open-1)

            return helper(idx+1, open+1) or helper(idx+1, open) or helper(idx+1, open-1)


        return helper(0, 0)
