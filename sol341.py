# class NestedIterator(object):


#     def __init__(self, nestedList):

#         self.flat = []
#         self.index = 0

#         def flatten(nested):

#             for item in nested:

#                 if item.isInteger():
#                     self.flat.append(item.getInetger())

#                 else:

#                     flatten(item.getList())

#         flatten(nestedList)


#     def next(self):

#         val = self.flat[self.index]
#         self.index += 1
#         return val
        

#     def hasNext(self):

        
#         return self.index < len(self.flat)


class NestedIterator(object):

    def __init__(self, nestedList):

        self.stack = list(reversed(nestedList))


    def next(self):

        return self.stack.pop().getInteger()
        

    def hasNext(self):

        while self.stack:
            top = self.stack[-1]

            if top.isInteger():
                return True

            self.stack.pop()
            self.stack.extend(reversed(top.getList()))

        return False