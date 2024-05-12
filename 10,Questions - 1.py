class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list = [None] * (3 * stack_size)
        self.pointers = [0, 0, 0]  # Stack pointers for each stack

    def push(self, stack_num, value):
        if self.pointers[stack_num - 1] < stack_num * self.stack_size:
            self.list[self.pointers[stack_num - 1]] = value
            self.pointers[stack_num - 1] += 1
        else:
            print("Stack Overflow")

    def pop(self, stack_num):
        if self.pointers[stack_num - 1] > (stack_num - 1) * self.stack_size:
            self.pointers[stack_num - 1] -= 1
            value = self.list[self.pointers[stack_num - 1]]
            self.list[self.pointers[stack_num - 1]] = None
            return value
        else:
            print("Stack Underflow")
            return None

    def print_stack(self, stack_num):
        start = (stack_num - 1) * self.stack_size
        end = stack_num * self.stack_size
        print(self.list[start:end])



three_stacks = ThreeStacks(3)
three_stacks.push(1, 1)
three_stacks.push(1, 2)
three_stacks.push(1, 3)
three_stacks.push(2, 4)
three_stacks.push(2, 5)
three_stacks.push(3, 6)

three_stacks.print_stack(1)  
three_stacks.print_stack(2) 
three_stacks.print_stack(3) 

print(three_stacks.pop(1))  
print(three_stacks.pop(2))
print(three_stacks.pop(3))  
