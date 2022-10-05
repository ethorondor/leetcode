'''
valid binary tree
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def is_valid_bst(root):
    
    def valid_node(node, left, right):
        if node is None:
            return True
        
        if not (node.value <right and node.value > left):
            return False
        
        return (valid_node(node.left, left, node.value) and valid_node(node.right, node.value, right))
    return valid_node(root, float('-inf'), float('inf')) 
        
root = node(5)
root.left = node(3)
root.right = node(7)
root.right.left = node(4)
root.right.right = node(8)

is_valid_bst(root)
# %%
