class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solver(rem, op, res):
            if rem == 0 and op == 0:
                ans.append("".join(res))

            if op > 0:
                res.append(')')
                solver(rem, op-1, res)
                res.pop()

            if rem > 0:
                res.append('(')
                solver(rem-1, op+1, res)
                res.pop()

        ans = []
        solver(n, 0, [])
        return ans