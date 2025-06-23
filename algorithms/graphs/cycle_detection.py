def has_cycle(adj_list):
    visited = set()
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif parent != neighbor:
                return True
        return False
    for node in adj_list:
        if node not in visited:
            if dfs(node, -1):
                return True
    return False
