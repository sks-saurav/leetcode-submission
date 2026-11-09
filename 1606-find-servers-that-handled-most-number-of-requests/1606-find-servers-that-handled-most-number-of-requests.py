class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        availableServer = SortedList([i for i in range(k)])
        requestCount = defaultdict(int)
        maxRequest = 0
        busyServer = []

        def pickServer(order):
            idx = availableServer.bisect_left(order)
            serverId = availableServer[0]
            if idx < len(availableServer):
                serverId = availableServer[idx]

            availableServer.remove(serverId)
            return serverId

        for i in range(len(arrival)):
            a = arrival[i]
            l = load[i]

            while busyServer and busyServer[0][0] <= a:
                time, serverId = heappop(busyServer)
                availableServer.add(serverId)

            # request dropped of no available server
            if len(availableServer) == 0: 
                continue

            pickedServerId = pickServer(i%k)
            requestCount[pickedServerId] += 1
            maxRequest = max(maxRequest, requestCount[pickedServerId])

            heappush(busyServer, (a+l ,pickedServerId))

        ans = []
        if maxRequest == 0:
            return ans

        for serverId in requestCount:
            if maxRequest == requestCount[serverId]:
                ans.append(serverId)

        return ans
