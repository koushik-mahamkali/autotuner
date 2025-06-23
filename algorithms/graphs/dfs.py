def dfs(adj_list, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in adj_list[start]:
        if neighbor not in visited:
            dfs(adj_list, neighbor, visited)
    return visited
