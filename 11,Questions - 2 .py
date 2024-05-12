class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Auxiliary stack to track minimum elements

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]



stack = MinStack()
stack.push(5)
print(stack.min())  
stack.push(6)
print(stack.min()) 
stack.push(3)
print(stack.min()) 
stack.push(7)
print(stack.min())  
stack.pop()
print(stack.min())  
stack.pop()
print(stack.min())  
