class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def dp(idx):
            if idx >= n:
                return 0

            width = shelfWidth
            curr_height = 0
            ans = int(1e9)

            while idx < n and width - books[idx][0] >= 0:
                width -= books[idx][0]
                curr_height = max(curr_height, books[idx][1])

                ans = min(ans, dp(idx+1) + curr_height)
                idx += 1

            return ans


        return dp(0)






            

                