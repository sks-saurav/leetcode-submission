class Solution:
    '''
    The problem states both players play optimally. This means Player 2 isn't making random moves; they are actively trying to make Player 1 lose.
   
    To represent optimal play in a 2-player turn-based game, you don't need a turn indicator. You just need a function that answers: "Can the current player win?"

    A player wins if they can make a move that reaches the total right now.
    A player also wins if they can make a move that forces the next player into a losing state (not can_win(...)).
    '''
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0: return True
            
        max_possible_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if max_possible_sum < desiredTotal: return False
            
        def can_win(mask, current_sum):
            if mask in memo:
                return memo[mask]
                
            for i in range(1, maxChoosableInteger + 1):
                if not (mask & (1 << i)):
                    
                    # Condition 1: Picking 'i' instantly reaches the target
                    if current_sum + i >= desiredTotal:
                        memo[mask] = True
                        return True
                        
                    # Condition 2: Picking 'i' forces the OPPONENT into a losing state
                    if not can_win(mask | (1 << i), current_sum + i):
                        memo[mask] = True
                        return True

            memo[mask] = False
            return False
                     
        memo = {}            
        return can_win(0, 0)