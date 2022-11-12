'''
valid binary search tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = node(1)
root.left = node(0)
root.right = node(2)

def valid_bst(root):
    def dfs(root, left, right):
        if root is None:
            return True
        if not (root.value<right and root.value>left):
            return False
        return (dfs(root.left, left, root.value) and dfs(root.right, root.value, right))
    return dfs(root, float('-inf'), float('inf'))
        
valid_bst(root)
# %%
