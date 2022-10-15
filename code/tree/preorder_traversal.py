'''
preorder traversal
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

def preorder_traversal(root):
    res = []
    def dfs(root):
        if root is None:
            return None
        res.append(root.value)
        dfs(root.left)
        dfs(root.right)
    dfs(root)
    return res

preorder_traversal(root)
# %%
