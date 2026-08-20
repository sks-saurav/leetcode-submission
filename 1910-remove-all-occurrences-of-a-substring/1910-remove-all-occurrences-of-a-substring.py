class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []

        def is_matching(st):
            d = len(st) - len(part)
            if d < 0:
                return False

            for i in range(len(part)):
                if st[d+i] != part[i]: return False

            return True

        for ch in s:
            stack.append(ch)
            if is_matching(stack):
                for _ in range(len(part)):
                    stack.pop()


        return ''.join(stack)