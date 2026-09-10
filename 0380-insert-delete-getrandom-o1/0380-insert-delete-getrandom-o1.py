class RandomizedSet:
    def __init__(self):
        self.lookup = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False

        self.arr.append(val)
        self.lookup[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lookup:
            return False

        i = self.lookup[val]
        j = len(self.arr)-1

        self.lookup[self.arr[j]] = i
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        
        self.arr.pop()
        del self.lookup[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()