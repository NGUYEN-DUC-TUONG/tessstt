class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            if not self.stack_enqueue:
                return None
            # Transfer elements from enqueue stack to dequeue stack to reverse the order
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop() if self.stack_dequeue else None


# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
print(queue.dequeue())  

queue.enqueue(4)
print(queue.dequeue())  
print(queue.dequeue())  
print(queue.dequeue())  
