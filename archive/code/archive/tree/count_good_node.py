'''
count good nodes
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = node(3)
root.left = node(1)
root.left.left = node(3)
root.right = node(4)
root.right.left = node(1)
root.right.right = node(5)

def count_good_nodes(root):
    res = [0]
    max_value = root.value
    def dfs(root, max_value):
        if root is None:
            return None
        if root.value >= max_value:
            res[0] += 1
        max_value = max(root.value, max_value)
        dfs(root.left, max_value)
        dfs(root.right, max_value)
    dfs(root, max_value)
    return res

count_good_nodes(root)
# %%
