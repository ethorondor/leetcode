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

def find_all_paths(root, s):
    if root is None:
        return False
    all_paths = []
    find_path(root, s, [], all_paths)
    return all_paths    
    
def find_path(root, s, current_path, all_paths):
    if root is None:
        return False
    current_path.append(root.value)
    if root.value == s and root.left is None and root.right is None:
        all_paths.append(list(current_path))
    else:
        find_path(root.left, s-root.value, current_path, all_paths)
        find_path(root.right, s-root.value, current_path, all_paths) 
    del current_path[-1]   
    
    
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(4)
root.right.left = tree_node(10)
root.right.right = tree_node(5)
s = 23
paths =find_all_paths(root, s)
# %%
