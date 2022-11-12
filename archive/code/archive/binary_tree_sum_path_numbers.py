'''
sum of path numbers
'''
#%%
class tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def paths_sum(root):
    paths_sum = 0
    sum = 0
    return find_path_sum(root, sum)
    
def find_path_sum(current_node, path_sum):
    if current_node is None:
        return 0
    
    path_sum = path_sum*10 + current_node.value
    if current_node.left is None and current_node.right is None:
        return path_sum
    
    return find_path_sum(current_node.left, path_sum) + find_path_sum(current_node.right, path_sum)

root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
root.right.left = tree_node(6)
root.right.right = tree_node(7)

paths_sum(root)
# %%
