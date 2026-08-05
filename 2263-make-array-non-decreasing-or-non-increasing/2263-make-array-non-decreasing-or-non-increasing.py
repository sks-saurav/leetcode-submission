class Solution:
    def convertArray(self, nums: List[int]) -> int:
        
        def cost_non_decreasing(arr):
            heap = []
            cost = 0

            for ele in arr:
                if heap and -heap[0] > ele:
                    last_ele = -heap[0]
                    cost += (last_ele - ele)
                    #Remove the old peak because we just paid to lower it
                    heapq.heappop(heap)
                    #Push the new "flattened" value to represent the lowered peak
                    heapq.heappush(heap, -ele)
                    
                heapq.heappush(heap, -ele)

            return cost


        a = cost_non_decreasing(nums)
        nums.reverse()
        b = cost_non_decreasing(nums)

        return min(a, b)