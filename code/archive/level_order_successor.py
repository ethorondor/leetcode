'''
level order successor for binary tree
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        
class solutions:
    def level_order(self, root, key):
        ans = []
        q = deque()
        q.append(root)
        while q:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            if current_node.value == key:
                break
        return q[0]
                    
                        
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(9)
root.right.left = tree_node(10)
root.right.right = tree_node(5)

s = solutions()
q = s.level_order(root, 12)
q.value
# %%
