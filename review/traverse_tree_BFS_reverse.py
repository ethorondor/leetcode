'''
traverse a tree with BFS backward
'''
#%%
from collections import deque
class tree_node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def traverse_tree_backward(root):
    q = deque()
    ans = []
    q.append(root)
    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            current_node = q.popleft()
            current_level.append(current_node.value)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        ans.insert(0,current_level)
    return ans
    
root = tree_node(12)
root.left = tree_node(7)
root.right = tree_node(1)
root.left.left = tree_node(9)
root.right.left = tree_node(10)
root.right.right = tree_node(5)
traverse_tree_backward(root)
# %%
