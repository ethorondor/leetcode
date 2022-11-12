'''
path with given sequence
'''
#%%
class tree_node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None
    
def find_given_path(root, path):
    if root is None:
        return len(path) == 0
    return find_path_recursive(root, path)
    
def find_path_recursive(current_node, path):
    if current_node is None:
        return False
    if path is None or current_node.value != path[0]:
        return False
    # find the right path
    if current_node.left is None and current_node.right is None and len(path) == 1:
        return True
    path.pop(0)
    return find_path_recursive(current_node.left, path) or find_path_recursive(current_node.right, path)

root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(9)
root.right.left = tree_node(10)
root.right.right = tree_node(5)
path = [12,7,9]
find_given_path(root, path)
# %%
