'''
breadth first search
'''
from collections import deque
def bfs(source_id, target):
    queue = deque()
    queue.append(source_id)
    
    visited = set()
    while queue:
        node = queue.popleft()
        if node == target:
            return True
     
        if node not in visited:
            visited.add(node) 
            for n in get_node(node).neighbors:
                queue.append(n)
    return False