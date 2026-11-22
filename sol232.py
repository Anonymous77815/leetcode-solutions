class MyQueue(object):

    def __init__(self):

        self.stack1 = []
        self.stack2 = []

    def push(self, x):

       self.stack1.append(x) 
        

    def pop(self):

        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        result = self.stack1.pop()

        self.stack1, self.stack2 = self.stack2, self.stack1

        return result
        

    def peek(self):

        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        result = self.stack1.pop()
        self.stack2.append(result)

        self.stack1, self.stack2 = self.stack2, self.stack1

        return result
        

    def empty(self):

        return len(self.stack1) == 0