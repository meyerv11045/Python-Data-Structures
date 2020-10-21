from node import Node
class Stack:
    def __init__(self,limit=1000):
        self.top = None
        self.size = 0
        self.limit = limit
    
    def get_top_node(self):
        return self.top

    def set_top_node(self,node):
        self.top = node

    def has_space(self):
        return self.limit > self.size

    def push(self,data):
        if not self.has_space(): raise OverflowError('Max Stack Size Reached')
        
        new_node = Node(data)
        if self.get_top_node() == None:
            self.set_top_node(new_node)
        else:
            new_node.set_next_node(self.top)
            self.set_top_node(new_node)

        self.size += 1

    def pop(self):
        if self.get_top_node() == None: 
            return None 
        else:
            result = self.get_top_node().get_data()
            self.set_top_node(self.get_top_node().get_next_node())
            self.size -= 1
            return result 

    def peek(self): 
        if self.get_top_node() == None: return None
        return self.get_top_node().get_data()

    def __len__(self):
        return self.size