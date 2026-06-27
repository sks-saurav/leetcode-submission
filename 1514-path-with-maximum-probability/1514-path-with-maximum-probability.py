class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        prob = [0.0] * n
        adj = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))

        heap = [(-1.0, start_node)]
        prob[start_node] = 1.0

        while heap:
            curr_prob, curr = heappop(heap)
            curr_prob = -1 * curr_prob
            if curr == end_node:
                return curr_prob

            for nb, nb_prob in adj[curr]:
                tprob = curr_prob * nb_prob
                if prob[nb] >= tprob:
                    continue
                prob[nb] = tprob
                heappush(heap, (-tprob, nb))

        return 0
