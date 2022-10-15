'''
level order traversal binary tree
'''
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