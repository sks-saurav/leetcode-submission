class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_char_set = set()
        for ch in source:
            source_char_set.add(ch)

        for ch in target:
            if ch not in source_char_set:
                return -1

        count = 1
        i = 0
        for j, ch in enumerate(target):
            while source[i] != ch:
                i += 1
                if i == len(source):
                    i = 0
                    count += 1

            i += 1
            if i == len(source) and j != len(target)-1:
                i = 0
                count += 1

        return count