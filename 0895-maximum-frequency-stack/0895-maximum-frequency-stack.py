from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.st = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        curr_freq = self.freq[val]
        self.max_freq = max(self.max_freq, curr_freq)
        self.st[curr_freq].append(val)

    def pop(self) -> int:
        if self.max_freq == 0:
            return -1

        ele = self.st[self.max_freq].pop()
        if len(self.st[self.max_freq]) == 0:
            self.max_freq-= 1
        
        self.freq[ele] -= 1
        return ele;