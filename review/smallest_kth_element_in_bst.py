'''
find smallest kth element in bst
'''
from lib2to3.pytree import Node


class node:
    def __init__(self, value):
        self.value = value
        self.left = Node
        self.right = Node
    
def find_path(root):
    if not root.left and not root.right:
        return root
    return find_path(root)
            
def smallest_kth_element(root):
    res = []
    find_path(root.left)
    res.append(root.value)
    find_path(root.right)    
    

root = node(5)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)