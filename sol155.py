class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value):
        self.stack.append(value)

        if not self.minStack:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value, self.minStack[-1]))
        

    def pop(self):

        if self.stack:
            self.stack.pop()
            self.minstack.pop()

        else:
            return "Empty stack"

    def top(self):

        if self.stack:
            return self.stack[-1]

        else:
            return "Empty Stack"

    def getMin(self):
        if self.stack:

            return self.minstack[-1]

        else:
            return "empty stack"


