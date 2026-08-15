class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def game_dp(st, end):
            if st == end:
                return nums[st]
            state = (st, end)
            if state in dp: return dp[state]

            left = nums[st] - game_dp(st+1, end)
            right = nums[end] - game_dp(st, end-1)

            ans = max(left, right)
            dp[state] = ans
            return ans

        dp = {}
        return game_dp(0, len(nums)-1) >= 0        