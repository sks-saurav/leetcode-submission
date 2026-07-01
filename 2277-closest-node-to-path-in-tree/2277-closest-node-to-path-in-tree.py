# PREMIUM

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Use BFS from each node to get all-pairs shortest paths
        dist = [[0] * n for _ in range(n)]
        for i in range(n):
            queue = deque([i])
            visited = {i}
            curr_dist = 0
            while queue:
                # Process level by level to track distance
                for _ in range(len(queue)):
                    curr = queue.popleft()
                    dist[i][curr] = curr_dist
                    for neighbor in adj[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
                curr_dist += 1

        # Process each query
        final_ans = []
        for start, end, node in query:
            parent = {start: -1}
            queue = deque([start])
            
            while queue:
                curr = queue.popleft()
                if curr == end:
                    break
                for neighbor in adj[curr]:
                    if neighbor not in parent:
                        parent[neighbor] = curr
                        queue.append(neighbor)
            
            # Reconstruct the path from end to start
            path = []
            curr = end
            while curr != -1:
                path.append(curr)
                curr = parent[curr]
            
            # Find the node on this path closest to 'node'
            ans_node_dist = float('inf')
            ans_node = start
            
            for pn in path:
                if dist[node][pn] < ans_node_dist:
                    ans_node_dist = dist[node][pn]
                    ans_node = pn
                    
            final_ans.append(ans_node)

        return final_ans