"""
stack = Stack(size)
stack.push(value)
value = stack.pop()
value = stack.peek()
stack.isEmpty()
"""

class Stack:
    def __init__(self, size):
        self.size = size
        self.pointer = -1
        self.buffer = [0] * size
    
    def push(self, value):
        if(self.pointer + 1 >= self.size):
            print("Out of array")
            return
        self.pointer += 1
        self.buffer[self.pointer] = value
        
    def pop(self):
        if(self.pointer == -1):
            print("Stack is empty")
            return
        value = self.buffer[self.pointer]
        self.pointer -= 1
        return value
    
    def peek(self):
        if(self.pointer == -1):
            print("Stack is empty")
            return
        value = self.buffer[self.pointer]
        return value
    
    def isEmpty():
        return self.pointer == -1