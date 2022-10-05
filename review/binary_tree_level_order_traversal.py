'''
binary tree level order traversal
'''
#%%
import collections
class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def level_order_traversal(root):
    res = []
    q = collections.deque()
    q.append(root)
    while q:
        leng = len(q)
        level = []
        for _ in range(leng):
            _tmp = q.popleft()
            level.append(_tmp.value)
            if _tmp.left:
                q.append(_tmp.left)
            if _tmp.right:
                q.append(_tmp.right)
        res.append(level)
    return res

root = node(0)
root.left = node(1)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(4)

level_order_traversal(root)
# %%
