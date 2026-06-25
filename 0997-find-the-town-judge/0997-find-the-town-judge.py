class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1 if len(trust) == 0 else -1
            
        trust_map = defaultdict(int)
        trust_rev_map = defaultdict(int)
        for a, b in trust:
            trust_map[b] += 1
            trust_rev_map[a] += 1


        for k in trust_map:
            if trust_map[k] >= n-1 and trust_rev_map[k] == 0:
                return k

        return -1
