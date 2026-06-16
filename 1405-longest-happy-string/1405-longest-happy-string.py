class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        counts = [[a, 'a'], [b, 'b'], [c, 'c']]
        
        while True:
            counts.sort(reverse=True)
            
            if counts[0][0] == 0:
                break
                
            if len(ans) >= 2 and ans[-1] == counts[0][1] and ans[-2] == counts[0][1]:
                if counts[1][0] == 0:
                    break
                
                ans.append(counts[1][1])
                counts[1][0] -= 1
                
            else:
                ans.append(counts[0][1])
                counts[0][0] -= 1
                
        return "".join(ans)

# import heapq

# class Solution:
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
#         heap = []
#         if a > 0: heapq.heappush(heap, (-a, 'a'))
#         if b > 0: heapq.heappush(heap, (-b, 'b'))
#         if c > 0: heapq.heappush(heap, (-c, 'c'))
        
#         ans = []
        
#         while heap:
#             count1, char1 = heapq.heappop(heap)
#             if len(ans) >= 2 and ans[-1] == ans[-2] == char1:
#                 if not heap:
#                     break

#                 count2, char2 = heapq.heappop(heap)
#                 ans.append(char2)
#                 count2 += 1  # Decrement magnitude (since it's negative)
                
#                 if count2 < 0:
#                     heapq.heappush(heap, (count2, char2))
                
#                 heapq.heappush(heap, (count1, char1))
                
#             else:
#                 ans.append(char1)
#                 count1 += 1
                
#                 if count1 < 0:
#                     heapq.heappush(heap, (count1, char1))
                    
#         return ''.join(ans)


