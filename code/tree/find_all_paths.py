'''
find all path
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
root = node(4)
root.left = node(2)
root.right = node(7)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(6)
root.right.right = node(9)

def find_all_paths(root):
    curr_path = []
    all_path = []
    def dfs(root, curr_path, all_path):
        curr_path.append(root.value)
        if root.left is None and root.right is None:
            all_path.append(list(curr_path))     
        else:
            if root.left:
                dfs(root.left, curr_path, all_path)
            if root.right:
                dfs(root.right, curr_path, all_path)
        del curr_path[-1]
    dfs(root, curr_path, all_path)
    return all_path

find_all_paths(root)
# %%
