class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)

        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)

        final_time = 0
        que = deque([(headID, 0)])
        while que:
            mgr, time = que.popleft()
            final_time = max(final_time, time)
            for emp in adj[mgr]:
                que.append((emp, time + informTime[mgr]))

        return final_time
