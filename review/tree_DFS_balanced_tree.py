'''
balanced tree
'''
#%%
class tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class solutions:
    def balanced_tree(self, root):
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1]-left[1])<=1)
            return (balanced, 1+max(left[1],right[1]))
        return dfs(root)
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.right.left = tree_node(5)
solution = solutions()
solution.balanced_tree(root)
# %%
