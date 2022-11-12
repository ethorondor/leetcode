'''
count the good nodes in a binary tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def count_good_nodes(root):
    def dfs(root, max_val):
        if root is None:
            return 0
        if root.value >= max_val:
            res = 1
        else:
            res = 0
        max_val = max(root.value, max_val)
        if root.left:
            res += dfs(root.left, max_val)
        if root.right:
            res += dfs(root.right, max_val)
        return res
    
    return dfs(root, root.value)
    

root = node(3)
root.left = node(1)
root.left.left = node(3)
root.right = node(4)
root.right.left = node(1)
root.right.right = node(5)
count_good_nodes(root)
# %%
