# from collections import deque

# class MyStack(object):

#     def __init__(self):
#         self.queue = deque()

#     def push(self, x):
#         self.queue.append(x)

#         for i in range(len(self.queue) - 1):
#             self.queue.append(self.queue.popleft())

#     def pop(self):
#         return self.queue.popleft()

#     def top(self):
#         return self.queue[0]

#     def empty(self):
#         return len(self.queue) == 0


from collections import deque

class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()
        self.q2.append(result)

        self.q1, self.q2 = self.q2, self.q1
        return result

    def empty(self):
        return len(self.q1) == 0
