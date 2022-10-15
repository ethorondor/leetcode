'''
lowest ancester binary tree
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
p = node(3)
q = node(7)

def lowest_common_ancestor(root, p, q):
    def dfs(root, p, q):
        if root is None:
            return None
        if root.value == p.value:
            return root
        if root.value == q.value:
            return root
        left = dfs(root.left, p, q)
        right = dfs(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
    return dfs(root, p, q)
r = lowest_common_ancestor(root, p, q)
# %%
