'''
find the diameter of a binary tree
'''
#%%
class tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class solutions:
    def diameter_of_binary_tree(self, root):
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2+left+right)
            
            return 1+max(left,right)
        dfs(root)
        return res[0]
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.right.left = tree_node(5)
solution = solutions()
solution.diameter_of_binary_tree(root)
# %%
