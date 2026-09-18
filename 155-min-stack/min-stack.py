class MinStack:

    def __init__(self):
        self.stack=[]
        self.mins = []
        self.min=1000

    def push(self, value: int) -> None:
        self.stack.append(value)
        if value < self.min:
            self.min = value
        if len(self.stack) >=2:
            if value < self.mins[len(self.stack)-2]:
                self.mins.append(value)
            else:
                self.mins.append(self.mins[len(self.stack)-2])
        else:
            self.mins.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack)-1]
        

    def getMin(self) -> int:
        return self.mins[len(self.mins)-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()