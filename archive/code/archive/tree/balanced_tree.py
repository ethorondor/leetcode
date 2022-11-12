'''
balanced tree
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

def balanced_tree(root):
    def dfs(root):
        if root is None:
            return [True, 0]
        left = dfs(root.left)
        right = dfs(root.right)
        balanced = (left[0] and right[0] and abs(left[1]-right[1])<= 1)
        return [balanced, 1 + max(left[0], right[0])]
    return dfs(root)[0]

balanced_tree(root)
# %%
