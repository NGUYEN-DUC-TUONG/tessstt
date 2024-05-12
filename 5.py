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
        

    def push(self, value):
        Node = Node(value)
        Node.next = self.linkedList.head
        self.linkedList.head = Node
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            Nodevalue = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return Nodevalue
        
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("-------")
customStack.pop()
print(customStack)