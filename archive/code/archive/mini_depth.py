'''
minimum depth of a binary tree
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
class solutions:
    def mini_depth(self, root):
        result = 0
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            result += 1
            for _ in range(q_len):
                current_node = q.popleft()
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
                if not current_node.left and not current_node.right:
                    return result
        return None
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)


s = solutions()
s.mini_depth(root)  
# %%
