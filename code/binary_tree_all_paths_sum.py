'''
find all paths sums to target
'''
#%%
class tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def find_all_paths(root, target):
    all_paths = []
    current_path = []
    find_paths_recursive(root, target, current_path, all_paths)
    return all_paths

def find_paths_recursive(current_node, target, current_path, all_paths):
    if current_node is None:
        return
    current_path.append(current_node.value)
    if current_node.value == target and current_node.left is None and current_node.right is None:
        all_paths.append(list(current_path))
    else:
        target -= current_node.value
        if current_node.left:
            find_paths_recursive(current_node.left, target, current_path, all_paths)
        if current_node.right:
            find_paths_recursive(current_node.right, target, current_path, all_paths)
    del current_path[-1]

root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
root.right.left = tree_node(6)
root.right.right = tree_node(7)

find_all_paths(root, 10)
# %%
