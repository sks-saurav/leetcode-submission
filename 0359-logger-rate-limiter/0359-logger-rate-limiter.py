class Logger:
    def __init__(self):
        self.last_time = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        ans = True
        if message in self.last_time:
            diff = timestamp - self.last_time[message]
            if diff < 10:
                ans = False

        if ans:
            self.last_time[message] = timestamp

        return ans


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)