class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        # bottoms up        
        # dp[i] stores the minimum height to place the first i books.
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            curr_width = 0
            curr_height = 0
            
            # Look backwards from the current book 'i' to see how many previous 
            # books we can group together on the same shelf.
            for j in range(i, 0, -1):
                curr_width += books[j-1][0]
                
                if curr_width > shelfWidth:
                    break
                
                curr_height = max(curr_height, books[j-1][1])
                
                dp[i] = min(dp[i], dp[j-1] + curr_height)
                
        return dp[n]


        # memoization
        # @cache
        # def dp(idx):
        #     if idx >= n:
        #         return 0

        #     width = shelfWidth
        #     curr_height = 0
        #     ans = int(1e9)

        #     while idx < n and width - books[idx][0] >= 0:
        #         width -= books[idx][0]
        #         curr_height = max(curr_height, books[idx][1])

        #         ans = min(ans, dp(idx+1) + curr_height)
        #         idx += 1
        #     return ans

        # return dp(0)





            

                