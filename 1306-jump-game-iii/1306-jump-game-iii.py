class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        n = len(arr)
        visited = [False] * n
        visited[start] = True
        que = deque([start])

        while que:
            curr = que.popleft()

            for nxt in (curr + arr[curr], curr - arr[curr]):
                if 0 <= nxt < n and not visited[nxt]:
                    if arr[nxt] == 0:
                        return True
                    visited[nxt] = True
                    que.append(nxt)

        return False

