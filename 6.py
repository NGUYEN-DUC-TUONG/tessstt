class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        Values = [str(x) for x in self.items]
        return ''.join(Values)
    
    def isEmpty(self):
        if self.items == []:
           return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "the is not any element in the Queue"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "the is not any element in the Queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
        
CustomQueue = Queue()
CustomQueue.enqueue(1)
CustomQueue.enqueue(2)
CustomQueue.enqueue(3)
print(CustomQueue.peek())
CustomQueue.delete()