class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        rc = [(rules[i][0], rules[i][1], costs[i]) for i in range(len(rules))]

        def match(i, p):
            if i + len(p) > len(source):
                return False, 0

            wild_count = 0
            for ch in p:
                if ch != '*' and source[i] != ch:
                   return False, 0
                if ch == '*':
                    wild_count += 1
                i += 1

            return True, wild_count

        @cache
        def helper(idx):
            if idx >= len(source):
                return 0

            ans = float('inf')
            if source[idx] == target[idx]:
                ans = helper(idx+1)

            for pattern, replacement, cost in rc:
                is_match, wild_count = match(idx, pattern)
                if is_match and replacement == target[idx: idx+len(replacement)]:
                    ans = min(ans, helper(idx+len(pattern)) + cost + wild_count) 

            return ans

        res = helper(0)
        return res if res != float('inf') else -1
                    