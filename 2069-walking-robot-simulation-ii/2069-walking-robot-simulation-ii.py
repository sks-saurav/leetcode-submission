from typing import List

class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.perimeter = 2 * (width - 1) + 2 * (height - 1)
        # Track a single 1D position along the perimeter loop
        self.pos = 0 
        self.initial = True

    def step(self, num: int) -> None:
        self.initial = False
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        p = self.pos
        
        # Bottom edge (Moving East)
        if p <= self.w - 1:
            return [p, 0]
        p -= (self.w - 1)
        
        # Right edge (Moving North)
        if p <= self.h - 1:
            return [self.w - 1, p]
        p -= (self.h - 1)
        
        # Top edge (Moving West)
        if p <= self.w - 1:
            return [self.w - 1 - p, self.h - 1]
        p -= (self.w - 1)
        
        # Left edge (Moving South)
        return [0, self.h - 1 - p]

    def getDir(self) -> str:
        if self.initial:
            return "East"
            
        # If pos is 0 after moving, it means it completed a loop
        # and arrived back at (0,0) by traveling South down the left edge.
        if self.pos == 0:
            return "South"
            
        # Otherwise, the direction maps directly to which edge it is on
        if self.pos <= self.w - 1:
            return "East"
        elif self.pos <= (self.w - 1) + (self.h - 1):
            return "North"
        elif self.pos <= 2 * (self.w - 1) + (self.h - 1):
            return "West"
        else:
            return "South"
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()