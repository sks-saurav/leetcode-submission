# PREMIUM

from collections import defaultdict
from typing import List

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def get_abv(word, level):
            if len(word) <= 3:
                return word
            wl = len(word) - 1 - level
            
            if wl <= 1: 
                return word
            return word[:level] + str(wl) + word[-1]

        # Track the current prefix level for every word independently
        levels = [1] * len(words) 
        
        abv_dict = defaultdict(list)
        for i in range(len(words)):
            abv = get_abv(words[i], levels[i])
            abv_dict[abv].append(i)

        flag = True
        while flag:
            flag = False
            for k in list(abv_dict.keys()):
                arr = abv_dict[k]
                if len(arr) == 1:
                    continue

                del abv_dict[k]
                for i in arr:
                    # Increment the exact level for this specific word
                    levels[i] += 1 
                    next_abv = get_abv(words[i], levels[i])
                    abv_dict[next_abv].append(i)

            for k in abv_dict:
                if len(abv_dict[k]) > 1:
                    flag = True

        ans = [""] * len(words)
        for k in abv_dict:
            idx = abv_dict[k][0]
            ans[idx] = k

        return ans