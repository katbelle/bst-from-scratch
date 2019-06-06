#build a BST from scratch
class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right 
    
    def __repr__(self):
        return f"Node({self.value}, {self.left}, {self.right})"

    def print_in_order(self):
        
        if self.left is not None: 
            # print(self.left.value)
            # lowest_value = self.left
            self.left.print_in_order()
        
        print(self.value)

        if self.right is not None:
            # print(self.right.value)
            self.right.print_in_order()

    def value_in_tree(self):
        pass
        
        
 
root_right = Node(10, Node(7,Node(5),Node(8)), Node(15))
root_right.print_in_order()
# print(root_right)

# my_node = Node(7,Node(5),Node(8))

# my_node.print_in_order()



#write a method which tells you if the tree has a given value.



