'''
level average in a binary tree
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
class solutions:
    def level_average(self, root):
        result = []
        # take care of edge case
        if root is None:
            return result
        q = deque()
        q.append(root)
        while q:
            current_level = []
            current_average = 0
            q_len = len(q)
            for _ in range(q_len):
                current_node = q.popleft()
                current_average += current_node.value/q_len
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            result.append(current_average)
        return result
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(8)
root.right.left = tree_node(10)
root.right.right = tree_node(5)
s = solutions()
s.level_average(root)
# %%
