'''
subtree of another tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root1 = node(3)
root1.left = node(4)
root1.right = node(5)
root1.left.left = node(1)
root1.left.right = node(2)
root2 = node(4)
root2.left = node(1)
root2.right = node(2)
def same_tree(root1, root2):
    def dfs(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None and root2:
            return False
        if root1 and root2 is None:
            return False
        if root1.value != root2.value:
            return False
        left = dfs(root1.left, root2.left)
        right = dfs(root1.right, root2.right)
        return left and right
    return dfs(root1, root2)
def subtree(root1, root2):
    if root1 is None:
        return False
    if same_tree(root1, root2):
        return True
    left = subtree(root1.left, root2)
    right = subtree(root1.right, root2)
    return left or right
subtree(root1, root2)
# %%
