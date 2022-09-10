'''
reverse level order traversal
'''
#%%
from collections import deque
from unittest import result
class tree_node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
class solutions:
    def reverse_traversal(self, root):
        result = deque()
        q = deque()
        if root is None:
            return result
        q.append(root)
        while q:
            q_len = len(q)
            current_level = []
            for _ in range(q_len):
                current_node = q.popleft()
                current_level.append(current_node.value)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            result.appendleft(current_level)
        return result
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(9)
root.right.left = tree_node(10)
root.right.right = tree_node(5)

s = solutions()
s.reverse_traversal(root)
# %%
