from node import Node

class LinkedList:
    def __init__(self,data=None):
        self.head = Node(data)
    
    def get_head_node(self):
        return self.head
    
    def set_head_node(self,head_node):
        self.head = head_node

    def append(self,data):
        new = Node(data)
        current = self.head

        while current.get_next_node() != None:
            current = current.get_next_node()

        current.set_next_node(new)

    def prepend(self,data):
        new = Node(data)
        new.set_next_node(self.get_head_node())
        self.set_head_node(new)

    def get_node(self,index):
        length = len(self)
        if index >= length:
            raise IndexError('Index Out of Range')
        
        cur_indx = 0 
        cur_node = self.head
        while cur_indx < length:
            if cur_indx == index: return cur_node.get_data()
            cur_indx += 1 
            cur_node = cur_node.get_next_node()

    def delete_node(self,index):
        length = len(self)
        if index >= length: 
            raise IndexError('Index Out of Range')

        cur_idx = 0
        cur_node = self.head
        while cur_idx < length:
            last_node = cur_node
            cur_node = cur_node.get_next_node()
            cur_idx += 1
            
            if cur_idx == index:
                last_node.set_next_node(cur_node.get_next_node())
            
    def __len__(self):
        current = self.head
        total = 0
        while current.get_next_node() != None:
            total += 1
            current = current.get_next_node() 
        return total
    
    def __str__(self):
        str_list = ''
        cur_node = self.get_head_node()
        while cur_node != None:
            str_list += str(cur_node.get_data()) + "\n"
            cur_node = cur_node.get_next_node()
        return str_list