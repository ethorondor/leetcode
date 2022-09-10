'''
zigzag traversal
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
    def zigzag_traversal(self, root):
        result = []
        q = deque()
        # take care of edge case
        if q is None:
            return q
        q.append(root)
        counter = 4
        while q:
            q_len = len(q)
            current_level = deque()
            for _ in range(q_len):
                current_node = q.popleft()
                if counter%2 == 0:
                    current_level.append(current_node.value)
                else:
                    current_level.appendleft(current_node.value)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            counter += 1
            result.append(list(current_level))
        return result
    
root = tree_node(1)
root.left = tree_node(2)
root.right = tree_node(3)
root.left.left = tree_node(4)
root.left.right = tree_node(5)
root.right.left = tree_node(6)
root.right.right = tree_node(7)

s = solutions()
s.zigzag_traversal(root)
# %%
