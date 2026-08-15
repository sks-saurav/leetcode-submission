class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        def game_dp(stones):
            # Base case: no stones left means the current player has no moves and loses            
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


        memo = {}
        return game_dp(n)