# PREMIUM

class Solution:
    def calculate(self, s: str) -> int:
        operators = set(['*', '/', '+', '-'])
        paran_end = {}
        stack = []
        for i, ch in enumerate(s):
            if ch == '(': stack.append(i)
            if ch == ')':
                paran_end[stack.pop()] = i

        def get_num(si):
            val = 0
            while si < len(s) and '0' <= s[si] <= '9':
                val = 10 * val + (ord(s[si]) - ord('0'))
                si += 1
            return val, si

        def divide(a, b):
            neg = a < 0 or b < 0
            a, b = abs(a), abs(b)
            val = a//b
            if neg:
                val = -1*val
            return val

        def eval_exp(st, end):
            stk = []
            last_op = '+'
            curr_val = 0
            while st <= end:
                curr_ch = s[st]
                if curr_ch in operators:
                    last_op = curr_ch
                    st += 1
                else:
                    if curr_ch == '(':
                        matching_bracket = paran_end[st]
                        curr_val = eval_exp(st+1, matching_bracket-1)
                        st = matching_bracket + 1
                    else:
                        curr_val, next_st = get_num(st)
                        st = next_st

                    # value update
                    if last_op == '-':
                        stk.append(-curr_val)
                    elif last_op == '+':
                        stk.append(curr_val)
                    elif last_op == '*':
                        pvs = stk.pop()
                        stk.append(pvs * curr_val)
                    elif last_op == '/':
                        pvs = stk.pop()
                        res = divide(pvs, curr_val)
                        stk.append(res)

            if not stk: return curr_val

            curr_val = 0
            while stk:
                curr_val += stk.pop()
            return curr_val

        return eval_exp(0, len(s)-1)

            
        