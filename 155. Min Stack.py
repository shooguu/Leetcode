class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.m = None
        self.index = 0


    def push(self, x: int) -> None:
        if self.m == None or self.m > x or self.index == 0:
            self.m = x
        self.stack.append((x, self.m))
        self.index += 1

    def pop(self) -> None:
        self.stack.pop()
        self.index -= 1
        if self.index > 0:
            self.m = self.stack[self.index - 1][1]

    def top(self) -> int:
        return self.stack[self.index - 1][0]

    def getMin(self) -> int:
        return self.stack[self.index - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
