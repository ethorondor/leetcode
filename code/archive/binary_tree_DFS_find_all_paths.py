'''
binary tree path sum
'''
#%%
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
def has_path(root, sum):
    if root is None:
        return False
    if root.left is None and root.right is None:
        if root.value == sum:
            return True
    return has_path(root.left, sum-root.value) or has_path(root.right, sum-root.value)
    

root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
root.right.left = tree_node(6)
root.right.right = tree_node(7)

has_path(root, 10)
# %%
