#Node is the basic unit of structure for a linked list
class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None #Pointer to the next node 

class linked_list:
    def __init__(self):
        self.head = node() #head node will not be accesible but will be used to point to 1st element 
    def append(self,data):
        new_node = node(data)
        cur = self.head
        #start at head and move to last node where a new node can be inserted
        while cur.next != None:
             cur = cur.next
        cur.next = new_node
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next 
        return total 
    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self,index):
        if index >= self.length():
            print("error: index out of range")
            return None 
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
    def delete(self,index):
        if index >= self.length():
            print("error: index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return None
            cur_idx += 1
