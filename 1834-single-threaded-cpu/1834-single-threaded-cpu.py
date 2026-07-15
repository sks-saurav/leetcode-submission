class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_arr = [(tasks[i][1], i, tasks[i][0]) for i in range(len(tasks))]
        task_arr.sort(key=lambda x:x[2])

        i = j = 0
        n = len(tasks)
        curr_time = task_arr[0][2]

        ans = []
        heap = []

        while len(ans) < n:
            while j < n and task_arr[j][2] <= curr_time:
                heappush(heap, task_arr[j])
                j += 1

            if heap:
                dur, pidx, st = heappop(heap)
                ans.append(pidx)
                curr_time += dur
            else:
                curr_time = task_arr[j][2]

        return ans

       


