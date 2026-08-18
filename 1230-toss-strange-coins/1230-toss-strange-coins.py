class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        
        def coin_toss(idx, head_count):
            if head_count > target:
                return 0.0

            if idx >= len(prob):
                return 1.0 if head_count == target else 0.0

            state = (idx, head_count)
            if state in memo: return memo[state]

            head = prob[idx] * coin_toss(idx+1, head_count + 1)
            tail = (1-prob[idx]) * coin_toss(idx+1, head_count)

            memo[state] = head + tail
            return memo[state]

        memo = {}
        return coin_toss(0, 0)
            