from LinkedList0 import LinkedList
from LinkedList0 import Node

class Stack:

    def __init__(self):
        self.stack = LinkedList()
    
    def push(self, x):
        n = Node(x)
        self.stack.add(n)
    
    def pop(self):
        popped = self.stack.last
        penultimate = self.stack.returnNodeAt(self.stack.length() - 2)
        penultimate.next = None
        return popped
    
    def print_stack(self):
        self.stack.printList()

  
