class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:

        if self.min_val > val:
            self.min_val = val
        self.my_stack.append((val, self.min_val))

    def pop(self) -> None:
        self.my_stack.pop()

        if len(self.my_stack) == 0:
            self.min_val = float('inf')
        else:
            self.min_val = self.my_stack[-1][1]

    def top(self) -> int:
        return 0 if len(self.my_stack) == 0 else self.my_stack[-1][0]

    def getMin(self) -> int:
        return self.my_stack[-1][1]

#[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
minStack = MinStack()
minStack.push(2147483646)
minStack.push(2147483646)
minStack.push(2147483647)
print(minStack.top())
minStack.pop()
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())
minStack.pop()
minStack.push(2147483647)
print(minStack.top ())
print(minStack.getMin())
minStack.push(-2147483648)
print(minStack.top())
print(minStack.getMin())
minStack.pop()
print(minStack.getMin())



[[],[-2],[-2],[-1],[],[],[],[]]


[(-2,-2),(-2,-2)]

[(-2,-2)]

[(-1,-2)]
