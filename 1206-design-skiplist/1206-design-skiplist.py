class ListNode:
    __slots__ = ('val', 'next', 'down')

    def __init__(self, val, next=None, down=None):
        self.val = val
        self.next = next
        self.down = down


class Skiplist:
    def __init__(self):
        # sentinel nodes to keep code simple
        level = ListNode(-math.inf, ListNode(math.inf))
        self.levels = [level]

    def search(self, target: int) -> bool:
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < target:
                node = node.next
            if node.next.val == target:
                return True
            level = node.down
        return False

    def add(self, num: int) -> None:
        stack = []
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            stack.append(node)
            level = node.down

        heads = True
        down = None
        while stack and heads:
            prev = stack.pop()
            node = ListNode(num, prev.next, down)
            prev.next = node
            down = node
            # flip a coin to stop or continue with the next level
            heads = random.randint(0, 1)

        # add a new level if we got to the top with heads
        if not stack and heads:
            node = ListNode(num, ListNode(math.inf), down)
            level = ListNode(-math.inf, node, self.levels[-1])
            self.levels.append(level)

    def erase(self, num: int) -> bool:
        found = False
        level = self.levels[-1]
        while level:
            node = level
            while node.next.val < num:
                node = node.next
            if node.next.val == num:
                found = True
                node.next = node.next.next
            level = node.down

        # remove the top level if it's empty
        while len(self.levels) > 1 and self.levels[-1].next.next is None:
            self.levels.pop()

        return found