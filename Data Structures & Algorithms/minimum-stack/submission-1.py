class MinStack:

    def __init__(self):
        self.s = []
        self.s_min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.s_min:
            if val <= self.s_min[-1]:
                self.s_min.append(val)
        else:
            self.s_min.append(val)
    
    def pop(self) -> None:
        s_pop = self.s.pop()
        if s_pop == self.s_min[-1]:
            self.s_min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_min[-1]
