class MinStack:
    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
    def pop(self) -> None:
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1] 
    def getMin(self) -> int:
        return self.stack[-1]

# MinStack(["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]])

minStack.push(-2)

