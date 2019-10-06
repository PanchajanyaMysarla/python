class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
        # if self.root > new_val:
        #     self.insert(self.root.left,new_val)
        # elif self.value < new_val:
        #     self.insert(self.root.right,new_val)
        # elif self == None:
        #     self.value = new_val
            
    def insert_helper(self,current,new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right,new_val)
            else:
                current.right = Node(new_val)
                
        elif current.value > new_val:
            if current.left:
                self.insert_helper(current.left,new_val)
            else:
                current.left = Node(new_val)
                
    def insert(self, new_val):
        self.insert_helper(self.root,new_val)

    def search_helper(self,current,find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right,find_val)
            else:
                return self.search_helper(current.left,find_val)
        return False
    def search(self, find_val):
        return self.search_helper(self.root,find_val)
        # if self.value > find_val:
        #     self.search(self.root.left,find_val)
        # elif self.value < new_value:
        #     self.search(self.root.right,find_val)
        # elif self.value == find_val:
        #     return True
        
       
        
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))