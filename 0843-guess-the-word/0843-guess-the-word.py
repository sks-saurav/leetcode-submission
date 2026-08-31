class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def get_count(a, b):
            return sum(1 for i, j in zip(a, b) if i == j)

        while words:
            best_word = ""
            min_worst_case = float('inf')

            # MINIMAX: Find the word that minimizes the worst-case remaining candidates
            for word in words:
                # Tally how many words would remain for each possible match score (0 to 5)
                score_counts = [0] * 7
                for n_word in words:
                    if word != n_word:
                        score_counts[get_count(word, n_word)] += 1
                
                # The worst-case scenario for 'word' is the highest tally
                worst_case = max(score_counts)

                if worst_case < min_worst_case:
                    min_worst_case = worst_case
                    best_word = word

            # Guess our mathematically safest word
            match = master.guess(best_word)

            if match == 6:
                return

            # Filter down to the valid candidates, exactly as you did!
            words = [w for w in words if get_count(best_word, w) == match]