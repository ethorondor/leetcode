'''
connect level order siblings
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value, left = Nonde, right = None):
        self.value = value
        self.left = left
        self.right = right
        
class solutions:
    def binary_tree_path_sum(self, root, s):
        q = deque()
        q.append(root)
        while q:
            q_len = len(q)
            current_node = q.popleft()
            # if the current node is a leaf
            if not current_node.left and not current_node.right:
                if current_node.value == s:
                    return True
            # or else
            else:
                s -= current_node.value
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
        return False