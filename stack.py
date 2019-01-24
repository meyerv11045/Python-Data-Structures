class Node:
    def __init__(self, d):
        self.data = d
        self.next = None 
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    def push(self,d): #Puts a new node onto the stack
        new_node = Node(d)
        if self.top:
           new_node.next = self.top
        self.top = new_node 
        self.size += 1
    def pop(self): #Removes top node from stak & returns it
        if self.top is None:
            return None 
        result = self.top.data
        self.top = self.top.next
        self.size -= 1
        return result 
    def peek(self): #Returns the data for the top node w/o changing the stack
        if self.top is None:
            return None
        return self.top.data 
