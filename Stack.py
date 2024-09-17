# Practicing stacks
from collections import deque
# initialize stack
stack = deque()
# pushing elements to the stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
# print the stack
# print(stack)
# creating custom stack class
class Stack:
    def __init__(self):
        self.stack = []
    # push operation
    def push(self,element):
        self.stack.append(element)
    # pop operation
    def pop(self):
        if not self.stack.is_empty(): 
            return self.pop()
        else:
            return "stack is empty"
    # peek operation
    def peek(self):
        if not self.stack.is_empty():
            return self.stack[-1]
        else:
            return "stack is empty"
    # check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    # return the size of stack
    def size(self):
        return len(self.stack)
stack = Stack()
stack.push(1)
print(stack)