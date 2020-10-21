class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next_node(self):
        return self.next_node

    def set_data(self,data):
        self.data = data 
    
    def set_next_node(self,next_node):
        self.next_node = next_node
    