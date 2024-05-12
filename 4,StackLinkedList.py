class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next
        
class linkedList:
    def __init__(self):
        self.head = None
        
class Stack:
    def __init__(self):
        self.linkedList = linkedList()

    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
        
customStack = Stack()
print(customStack.isEmpty())