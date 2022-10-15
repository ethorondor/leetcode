'''
find lowest common ancestor binary search tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def lowest_common_ancestor(root, p, q):
    if root.value == p.value or root.value == q.value:
        return root
    if root.left is None and root.right is None:
        return None
    if root.left:
        left = lowest_common_ancestor(root.left, p ,q)
    if root.right:
        right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    else:
        return left or right
    
p = node(4)
q = node(8)    
root = node(6)
root.left = node(2)
root.right = node(8)
root.left.left = node(0)
root.left.right = node(4)
root.right.left = node(7)
root.right.right = node(9)
r = lowest_common_ancestor(root, p, q)
# %%
