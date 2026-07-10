# #PREMIUM 


class Solution:
    def evaluateExpression(self, expression: str) -> int:
        matching_comma = {}
        stack = []
        i = 0

        # Precompute matching commas for each operator
        while i < len(expression):
            ch = expression[i]
            if ch in ('a', 's', 'm', 'd'):
                stack.append(i)
                i += 2  # skip to the parenthesis
            elif ch == ',':
                matching_comma[stack.pop()] = i
            i += 1

        def apply_operator(a, b, operator):
            if operator == 'add':
                return a + b
            elif operator == 'sub':
                return a - b
            elif operator == 'mul':
                return a * b
            elif operator == 'div':
                return int(a / b) # Safely handles negative division in Python

        def eval_exp(start, end):
            if start >= end:
                return 0

            isNeg = False
            idx = start

            # Check for negative sign
            if expression[idx] == '-':
                isNeg = True
                idx += 1
            
            # Check if it's a pure number
            if '0' <= expression[idx] <= '9':
                val = 0
                while idx < end and '0' <= expression[idx] <= '9':
                    val = 10 * val + (ord(expression[idx]) - ord('0'))
                    idx += 1
                return -val if isNeg else val

            # Otherwise, it must be an operator
            operator = expression[idx:idx+3]
            split_idx = matching_comma[idx]

            # operand_a is from idx+4 to split_idx
            # operand_b is from split_idx+1 to end-1 (excluding the closing parenthesis)
            a = eval_exp(idx+4, split_idx)
            b = eval_exp(split_idx+1, end-1)
            
            return apply_operator(a, b, operator)

        return eval_exp(0, len(expression))
      