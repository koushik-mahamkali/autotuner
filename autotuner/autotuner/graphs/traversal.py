from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend(graph.get(node, []))
    return order

def dfs(graph, start):
    visited = set()
    order = []

    def dfs_helper(v):
        if v not in visited:
            visited.add(v)
            order.append(v)
            for neighbor in graph.get(v, []):
                dfs_helper(neighbor)

    dfs_helper(start)
    return order