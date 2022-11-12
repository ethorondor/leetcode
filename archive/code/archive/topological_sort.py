'''
topological sort
'''
#%%
from collections import deque
def topological_sort(vertices, edges):
    sorted_order = []
    # initialize the graph
    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}
    # building graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1
    
    # find all sources, all vertices with 0-degree
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
            
    # for each source, add it to the sorted order and substract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    if len(sorted_order) != vertices:
        return []
    return sorted_order

r = topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
# %%
