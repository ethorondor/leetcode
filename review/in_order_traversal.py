'''
in order traversal
'''
#%%
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class solutions:
    def in_order_traversal(self, root):
        res = []
        
        def in_order(root):
            if root is None:
                return
            in_order(root.left)
            res.append(root.value)
            in_order(root.right)
        in_order(root)
        return res            
        
root = node(5)
root.left = node(2)
root.right = node(6)
root.left.left = node(1)
root.left.right = node(3)
s = solutions()
s.in_order_traversal(root)
# %%
