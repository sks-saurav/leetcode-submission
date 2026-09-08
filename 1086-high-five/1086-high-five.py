class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for s_id, score in items:
            adj[s_id].append(score)

        ans = []
        for k in adj:
            adj[k].sort(reverse=True)
            scores = adj[k][:5]
            avg = sum(scores)//len(scores)
            ans.append([k, avg])

        return sorted(ans)