import heapq
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(graph):
    result = []
    i, e = 0, 0
    edges = sorted(graph['edges'], key=lambda item: item[2])
    parent = []
    rank = []

    for node in range(graph['V']):
        parent.append(node)
        rank.append(0)

    while e < graph['V'] - 1:
        u, v, w = edges[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    return result

def prim(graph, start):
    visited = set()
    mst = []
    edges = [(0, start, start)]
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for to, w in graph[v]:
                if to not in visited:
                    heapq.heappush(edges, (w, v, to))
    return mst