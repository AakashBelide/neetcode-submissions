class MinStack:

    def __init__(self):
        self.min_stack1 = []
        self.min_stack2 = []

    def push(self, val: int) -> None:
        self.min_stack1.append(val)
        if (not self.min_stack2) or (self.min_stack2 and self.min_stack2[-1]>=val):
            self.min_stack2.append(val)

    def pop(self) -> None:
        tmp = self.min_stack1.pop()
        if self.min_stack2[-1]==tmp:
            self.min_stack2.pop()

    def top(self) -> int:
        return self.min_stack1[-1]

    def getMin(self) -> int:
        if self.min_stack2:
            return self.min_stack2[-1]
