from collections import deque
def bfs(adj_list, start_node):
    visited = set()
    queue = deque([start_node])
    order = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in adj_list.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return order
