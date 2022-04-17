from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)


def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reverse = ""
    for char in range(stack.size()):
        reverse += stack.pop()
    return reverse


def is_balanced(string):
    parantheses = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    stck = Stack()
    for char in string:
        if char in parantheses.keys():
            stck.push(char)
        if char in parantheses.values():
            if stck.size() == 0:
                return False
            if parantheses[stck.pop()] != char:
                return False
    return True
 