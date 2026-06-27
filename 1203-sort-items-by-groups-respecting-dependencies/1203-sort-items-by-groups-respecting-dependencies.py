from collections import defaultdict, deque
from typing import List

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # 1. Assign isolated items (-1) to their own unique groups
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        # 2. Initialize graphs and in-degree arrays for BOTH items and groups
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        
        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m
        
        # 3. Populate graphs and in-degrees
        for item in range(n):
            for b_item in beforeItems[item]:
                # Build global item dependency graph
                item_graph[b_item].append(item)
                item_indegree[item] += 1
                
                # Build global group dependency graph (only if they are different groups)
                g_item = group[item]
                g_b_item = group[b_item]
                if g_item != g_b_item:
                    group_graph[g_b_item].append(g_item)
                    group_indegree[g_item] += 1
        
        # 4. Reusable global topological sort function
        def topo_sort(graph, indegree, num_nodes):
            que = deque([i for i in range(num_nodes) if indegree[i] == 0])
            order = []
            
            while que:
                curr = que.popleft()
                order.append(curr)
                for nxt in graph[curr]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        que.append(nxt)
                        
            return order if len(order) == num_nodes else []
        
        # 5. Perform sorting globally on both levels
        item_order = topo_sort(item_graph, item_indegree, n)
        group_order = topo_sort(group_graph, group_indegree, m)
        
        # If either sort fails (cycle detected), there's no valid ordering
        if not item_order or not group_order:
            return []
        
        # 6. Group the globally sorted items into their respective group buckets
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)
            
        # 7. Assemble the final answer using the globally sorted group order
        final_order = []
        for g in group_order:
            final_order.extend(group_to_items[g])
            
        return final_order