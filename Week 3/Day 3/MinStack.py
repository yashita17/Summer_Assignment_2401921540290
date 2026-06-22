class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, value):
        self.stack.append(value)
        if self.minstack == [] or value <= self.minstack[-1]:
            self.minstack.append(value)
        
        

    def pop(self):
        popped = self.stack.pop()
        if popped == self.minstack[-1]:
            self.minstack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minstack[-1]