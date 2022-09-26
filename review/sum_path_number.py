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

def find_sum_of_paths(root):
    ans = []
    current_number = 0
    find_path(root, current_number, ans)
    return sum(ans)

def find_path(root, current_number, ans):
    if root is None:
        return None
    current_number = 10*current_number + root.value
    if root.left is None and root.right is None:
        ans.append(current_number)
    else:
        find_path(root.left, current_number, ans)
        find_path(root.right, current_number, ans)
    current_number = current_number//10
    
    
root = tree_node(2)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(4)
root.right.left = tree_node(7)
root.right.right = tree_node(5)
s = 23
paths =find_sum_of_paths(root)
# %%
