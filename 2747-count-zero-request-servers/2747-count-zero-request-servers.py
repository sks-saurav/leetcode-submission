class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        track = defaultdict(int)
        ans = [0] * len(queries)
        ist, iend = 0, 0
        logs.sort(key=lambda x: x[1])
        qidx = {val : i for i, val in enumerate(queries)}
        queries.sort()

        for tend in queries:
            tst = tend-x
            while iend < len(logs) and logs[iend][1] <= tend:
                server_id = logs[iend][0]
                track[server_id] += 1
                iend += 1

            while ist < len(logs) and logs[ist][1] < tst:
                server_id = logs[ist][0]
                if track[server_id] == 1:
                    del track[server_id]
                else:
                    track[server_id] -= 1
                ist += 1

            idle_server = n - len(track)
            aidx = qidx[tend]
            ans[aidx] = idle_server

        return ans




