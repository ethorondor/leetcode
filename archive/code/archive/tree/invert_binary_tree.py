'''
invert a binary tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def invert_binary_tree(root):
    def dfs(root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left:
            left = dfs(root.left)
        if root.right:
            right = dfs(root.right)
        if left and right:
            root.left, root.right = root.right, root.left
        return root 
    return dfs(root)        

def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
    
root = node(4)
root.left = node(2)
root.right = node(7)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(6)
root.right.right = node(9)
r = invert_tree(root)
# %%
root = node(1)
root.left = node(2)
r = invert_tree(root)
# %%
