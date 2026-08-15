import sys

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # sys.setrecursionlimit(200000)
        
        memo = {}
        
        def game_dp(stones):
            if stones == 0:
                return False
                
            if stones in memo: return memo[stones]
            
            limit = int(stones ** 0.5)
            
            for val in range(1, limit + 1):
                taken_stone = val * val
                
                # If removing this square leaves the opponent in a losing state (False),
                # then this current state is a winning state (True) for us.
                if not game_dp(stones - taken_stone):
                    memo[stones] = True
                    return True
                    
            memo[stones] = False
            return False

        return game_dp(n)