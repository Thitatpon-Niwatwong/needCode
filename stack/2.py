class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minstack[-1]


A = MinStack()
A.push(-2)
A.push(0)
A.push(-3)
print(A.getMin())  # Output: -3
A.pop()
print(A.top())     # Output: 0
print(A.getMin())  # Output: -2
