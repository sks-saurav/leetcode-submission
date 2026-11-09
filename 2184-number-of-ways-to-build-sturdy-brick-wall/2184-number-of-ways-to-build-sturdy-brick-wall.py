class Solution:
    def buildWall(self, height: int, width: int, bricks: list[int]) -> int:
        MOD = int(1e9) + 7
        allPerm = []
        def getAllPerm(currW, taken):
            if currW > width: return
            if currW == width:
                allPerm.append(taken)
                return

            for brick in bricks:
                newW = currW + brick
                if newW > width: continue
                tempTaken = taken
                if newW != width:
                    tempTaken = taken | (1 << (newW-1))
                getAllPerm(newW, tempTaken)

        getAllPerm(0, 0)
        adj = defaultdict(list)
        n = len(allPerm)
        if n == 0:
            return 0

        for i in range(n):
            for j in range(i, n):
                if (allPerm[i] & allPerm[j]) == 0:
                    adj[i].append(j)
                    if i != j:
                        adj[j].append(i)

        @cache
        def count_ways(u: int, rem_height: int) -> int:
            if rem_height == 1:
                return 1

            total = 0
            for v in adj[u]:
                total = (total + count_ways(v, rem_height - 1)) % MOD
            return total

        ans = 0
        for i in range(n):
            ans = (ans + count_ways(i, height)) % MOD

        return ans

            


