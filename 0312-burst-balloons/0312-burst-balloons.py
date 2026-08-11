class Solution:
    '''
    Think backword, what baloon will remain last, then second last and so on...
    https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0pwFf-BnpkXxs0Ra0eU2sJY&index=25
    '''
    def maxCoins(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        arr = [1]
        for ele in nums:
            arr.append(ele)
        arr.append(1)
        dp = {}

        def get_max_coin(i, j):
            if i > j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            ans = float('-inf')
            for k in range(i, j+1):
                coin = arr[i-1] * arr[k] * arr[j+1]
                coin += (get_max_coin(i, k-1) + get_max_coin(k+1, j))
                ans = max(coin, ans)

            dp[(i,j)] = ans
            return ans

        return get_max_coin(1, len(nums))



        