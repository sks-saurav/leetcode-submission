class Solution:
    def parseTernary(self, expression: str) -> str:
        split = {}
        stack = []

        for i, ch in enumerate(expression):
            if ch == '?': stack.append(i)
            if ch == ':':
                split[stack.pop()] = i


        def solve(st, end):
            if st == end:
                return expression[st]

            op = expression[st]
            q_idx = st+1
            col_idx = split[q_idx]
            if op == 'T':
                return solve(q_idx+1, col_idx-1)
            else:
                return solve(col_idx+1, end)

        return solve(0, len(expression)-1)