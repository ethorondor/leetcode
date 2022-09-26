'''
binary tree sum
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def has_path(root, s):
    if root is None:
        return False
    if root.value == s and root.left is None and root.right is None:
        return True
    return has_path(root.left, s-root.value) or has_path(root.right, s-root.value)
    
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(9)
root.right.left = tree_node(10)
root.right.right = tree_node(5)
has_path(root, 12)