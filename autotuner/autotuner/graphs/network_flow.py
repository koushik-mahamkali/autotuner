from collections import deque

def bfs_capacity(residual_graph, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v in residual_graph[u]:
            if v not in visited and residual_graph[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    residual_graph = {u: {} for u in graph}
    for u in graph:
        for v in graph[u]:
            residual_graph[u][v] = graph[u][v]
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0

    parent = {}
    max_flow = 0

    while bfs_capacity(residual_graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

def edmonds_karp(graph, source, sink):
    from collections import deque
    residual = {u: {} for u in graph}
    for u in graph:
        for v in graph[u]:
            residual[u][v] = graph[u][v]
            if v not in residual:
                residual[v] = {}
            if u not in residual[v]:
                residual[v][u] = 0

    def bfs():
        parent = {source: None}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in residual[u]:
                if v not in parent and residual[u][v] > 0:
                    parent[v] = u
                    if v == sink:
                        return parent
                    queue.append(v)
        return None

    max_flow = 0
    while True:
        parent = bfs()
        if not parent:
            break
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow

def dinic(graph, source, sink):
    from collections import deque
    level = {}
    capacity = {u: dict(graph[u]) for u in graph}
    for u in graph:
        for v in graph[u]:
            if v not in capacity:
                capacity[v] = {}
            if u not in capacity[v]:
                capacity[v][u] = 0

    def bfs():
        nonlocal level
        level = {source: 0}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in capacity[u]:
                if v not in level and capacity[u][v] > 0:
                    level[v] = level[u] + 1
                    queue.append(v)
        return sink in level

    def dfs(u, flow):
        if u == sink:
            return flow
        for v in capacity[u]:
            if level.get(v) == level[u] + 1 and capacity[u][v] > 0:
                pushed = dfs(v, min(flow, capacity[u][v]))
                if pushed:
                    capacity[u][v] -= pushed
                    capacity[v][u] += pushed
                    return pushed
        return 0

    max_flow = 0
    while bfs():
        flow = dfs(source, float('inf'))
        while flow:
            max_flow += flow
            flow = dfs(source, float('inf'))
    return max_flow