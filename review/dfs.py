'''
depth first search
'''
def dfs(source, target):
    return dfs_helper(source, target, set())

def dfs_helper(source, target, visited):
    if source == target:
        return True
    if source in visited:
        return False
    visited.add(source)
    # find all neighbor of source
    source = get_node(source)
    for node in source.neighbors:
        if dfs_helper(node, target, visited):
            return True
    return False