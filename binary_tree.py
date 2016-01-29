'''
Created on 28 sty 2016

BST - my first python program :)

@author: stanek
'''

class Node:
    
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 
        
    def add_node(self, data):
        if self.data > data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add_node(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add_node(data)
            
    def print_nodes(self):
        if self.left is not None:
            self.left.print_nodes()
        print(self);
        if self.right is not None:
            self.right.print_nodes()
    
    def __str__(self):
        return str(self.data)
    
class binary_tree:
    
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root
                   
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.add_node(data)
                
    def print_all(self):
        if self.root is None:
            print("Empty tree")
        else:
            self.root.print_nodes();
        
        
if __name__ == '__main__':
    b = binary_tree();
    b.add(1)
    b.add(2)
    b.add(4)
    b.add(6)
    b.add(3)
    b.add(5)
    b.print_all()
