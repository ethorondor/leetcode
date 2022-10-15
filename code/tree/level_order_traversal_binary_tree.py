'''
level order traversal binary tree
'''
#%%
from collections import deque
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

def level_order_traversal(root):
    q = deque()
    q.append(root)
    res = []
    while q:
        _len = len(q)
        level = []
        for _ in range(_len):
            _node = q.popleft()
            level.append(_node.value)
            if _node.left:
                q.append(_node.left)
            if _node.right:
                q.append(_node.right)
        res.append(level)
    return res
level_order_traversal(root)
# %%
