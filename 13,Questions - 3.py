class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
            return True
        return False

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


class SetOfStacks:
    def __init__(self, capacity_per_stack):
        self.capacity_per_stack = capacity_per_stack
        self.stacks = []

    def push(self, item):
        if not self.stacks or self.stacks[-1].is_full():
            new_stack = Stack(self.capacity_per_stack)
            new_stack.push(item)
            self.stacks.append(new_stack)
        else:
            self.stacks[-1].push(item)

    def pop(self):
        if not self.stacks:
            return None
        item = self.stacks[-1].pop()
        if self.stacks[-1].is_empty():
            self.stacks.pop()
        return item

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            return None
        item = self.stacks[index].pop()
        if self.stacks[index].is_empty():
            self.stacks.pop(index)
        return item



set_of_stacks = SetOfStacks(capacity_per_stack=3)
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)

print(set_of_stacks.pop())  
print(set_of_stacks.popAt(0))  
print(set_of_stacks.pop())  
print(set_of_stacks.pop())  
