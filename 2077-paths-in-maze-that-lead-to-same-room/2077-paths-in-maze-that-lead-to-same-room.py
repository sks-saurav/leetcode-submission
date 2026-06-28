class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        adj = defaultdict(set)
        for a, b in corridors:
            adj[a].add(b)
            adj[b].add(a)
        
        # def count_three_len_cycle(u, pu, dist, root):
        #     if dist > 3: return 0
        #     if dist == 3:
        #         return 1 if u == root else 0

        #     ans = 0
        #     for v in adj[u]:
        #         if v != pu:
        #             ans += count_three_len_cycle(v, u, dist+1, root)
        #     return ans

        def count_three_len_cycle(node):
            res = 0
            nb = list(adj[node])
            for i in range(len(nb)):
                for j in range(i+1, len(nb)):
                    a, b = nb[i], nb[j]
                    if a in adj[b]:
                        res += 1

            return res
            

        final_ans = 0
        for node in range(1, n+1):
            final_ans += count_three_len_cycle(node)
        return final_ans//3