from collections import deque

class MinStack:

    def __init__(self):
        self.min_ = deque()
        self.stack_ = deque()
        self.size = 0

    def push(self, val: int) -> None:
        self.stack_.append(val)

        if self.size > 0:
            if val <= self.min_[-1]:
                self.min_.append(val)
        else:
            self.min_.append(val)

        self.size += 1

    def pop(self) -> None:
        if self.size > 0:
            popped_ele = self.stack_.pop()
            self.size -=1

            if self.min_[-1] == popped_ele:
                self.min_.pop()

    def top(self) -> int:
        if self.size > 0:
            return self.stack_[-1]

    def getMin(self) -> int:
        if self.size > 0:
            return self.min_[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
