class node:
    def __init__(self,value=None):
        self.value = value 
        self.left_child = None
        self.right_child = None 
        self.parent = None 
class binary_search_tree:
    def __init__(self):
        self.root = None #Starting node at the top of the tree
    
    def insert(self,value):
        if self.root == None: #Checks if root node is empty and if so it fills the root node
            self.root = node(value)
        else:
            self._insert(value,self.root) #Otherwise it calls a recursive, private function to place the value on the tree 
            
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None: #If there is no left child, it creates a new node and sets it = to the left child
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node #Setting the parent 
            else: #Otherwise if there is a left child it continues down the tree w/ a recursive call 
                self._insert(value,cur_node.left_child)           
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node #Setting the parent 
            else:
                self._insert(value,cur_node.right_child)    
        else:
            print("Value Already in tree!")   

    def print_tree(self): #Prints it in order (somehow)
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child) 

    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height): #Dont quite understand how it works 
        if cur_node == None:  #Base case 
            return cur_height
        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)
    
    def find(self,value): #Returns the node/location of a value 
        if self.root != None:
            return self._find(value,self.root)
        else:
            return None 
    
    def _find(self,value,cur_node):
        if value == cur_node: #Base Case
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value,cur_node.right_child)

    def delete_value(self,value):
        return self.delete_node(self.find(value))
    
    def delete_node(self,node):
        #Returns the (leaf) node w/ the min value in a tree rooted at input node
        def min_value_node(node):
            current = node
            while current.left_child != None: #Only have to move down left side since trees go from least (L) to greatest (R)
                current = current.left_child 
            return current
        #Returns the number of children (1 or 0) for a specified node
        def num_children(node):
            num = 0
            if node.left_child != None: 
                num += 1
            if node.right_child != None:
                num += 1
            return num
        
        node_parent = node.parent #Get parent node of node to be deleted
        node_children = num_children(node) #Get num of children of node to be deleted
        
        #CASE 1 (Node has no children)
        if node_children == 0:
            #Remove reference to the node from the parent object 
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None 
        #CASE 2 (Node has a single child)
        if node_children == 1:
            #Get the child node
            if node.left_child != None:
                child = node.left_child
            else:
                child = node.right_child
            #Replace node to be deleted w/ its child
            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child 
            #Correct the parent pointer in the node 
            child.parent = node_parent
        #CASE 3 (Node has 2 children)
        if node_children == 2:
            #Get the inorder (next greatest) successor of the deleted node
            successor = min_value_node(node.right_child)
            #Copy the successor's value into the node we wish to delete
            node.value = successor.value
            #Recursively delete the successor since its value has been copied into node, essentially deleting the node's previous value 
            self.delete_node(successor)


    def search(self,value): #Returns T/F if the value is located in the tree
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value == cur_node.value: #Base Case
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        else:
            return False

def fill_tree(tree,num_elems=100,max_int=1000):
    from random import randint
    for x in range(num_elems):
        x = randint(0,max_int)
        tree.insert(x)
    return tree

def validate_bst(root, min, max): #Ensures values in the tree are smaller on the left and larger on the right
    if root == None:
        return True
    #Makes sure the value isnt larger on the left or smaller on the right
    if (root.value > min and root.value < max and 
        validate_bst(root.left_child,min,root.value) and 
        validate_bst(root.right_child,root.value,max)):
        return True 
    else:
        return False