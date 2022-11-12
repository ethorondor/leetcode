'''
diameter of a tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def diameter_of_tree(root):
    diameter = [0]
    def dfs(root):
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        diameter[0] = max(diameter[0], left+right)
        return 1 + max(left, right)
    dfs(root)
    return diameter[0]
    
root = node(4)
root.left = node(2)
root.right = node(7)
root.left.left = node(1)
root.left.right = node(3)
root.right.left = node(6)
root.right.right = node(9)

diameter_of_tree(root)    
# %%
