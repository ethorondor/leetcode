'''
find maximum depth of a binary tree
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

def max_depth(root):
    depth = 0
    if root is None:
        return depth
    def dfs(root, depth):
        if root.left is None and root.right is None:
            return depth
        if root.left:
            left = dfs(root.left, depth+1)
        if root.right:
            right = dfs(root.right, depth+1)
        depth = max(left, right)
        return depth
    return dfs(root, depth)

def maximum_depth(root):
    max_depth = [0]
    def dfs(root):
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        max_depth[0] = 1+max(left, right)
        return max_depth[0]
    dfs(root)
    return max_depth[0]
maximum_depth(root)
# %%
