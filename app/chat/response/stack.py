

class Stack():

    """ stack for multiplication chatbot"""

    def __init__(self):
        self.stack = list()

    def push(self, data):
        # allow duplicates
        self.stack.append(data)
        return True

    def pop(self):
        if len(self.stack) <=0:
            return "Stack empty"
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def view(self):
        for item in self.stack:
            print(format(item))

