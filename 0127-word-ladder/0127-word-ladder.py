class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = set(word_list)
        if end_word not in word_set:
            return 0

        seen = set()
        que = deque([(begin_word, 1)])
        seen.add(begin_word)
        lower_alpha = 'abcdefghijklmnopqrstuvwxyz'

        while que:
            curr_word, step = que.popleft()
            if curr_word == end_word:
                return step

            curr_arr = [ch for ch in curr_word]
            for i in range(len(curr_arr)):
                for rch in lower_alpha:
                    curr_arr[i] = rch
                    new_word = ''.join(curr_arr)
                    if not new_word in seen and new_word in word_set:
                        seen.add(new_word)
                        que.append((new_word, step+1))
                curr_arr[i] = curr_word[i]

        return 0

        
            
