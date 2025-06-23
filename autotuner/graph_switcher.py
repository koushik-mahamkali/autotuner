from algorithms.graphs.bfs import bfs
from algorithms.graphs.dfs import dfs
from algorithms.graphs.union_find import UnionFind
from algorithms.graphs.cycle_detection import has_cycle
from algorithms.graphs.dijkstra_heap import dijkstra_heap
from algorithms.graphs.dijkstra_matrix import dijkstra_matrix
from algorithms.graphs.toposort import topo_sort
from autotuner.graph_features import get_graph_features
def choose_graph_algorithm(
    adj_list,
    algo="auto",
    matrix=False,
    detect_cycle=False,
    use_union_find=False,
    use_topo_sort=False,
    run_all=False
):
    features = get_graph_features(adj_list)
    num_nodes = features["num_nodes"]

    if run_all:
        return {
            "algorithm": "all_algorithms",
            "features": features,
            "output": {
                "bfs": bfs(adj_list, 0),
                "dfs": dfs(adj_list, 0),
                "cycle_detected": has_cycle(adj_list),
                "dijkstra_heap": dijkstra_heap(adj_list, 0),
                "dijkstra_matrix": dijkstra_matrix(adj_list, 0),
                "union_find_cycle": run_union_cycle_check(adj_list, num_nodes),
                "topo_sort": topo_sort(adj_list, num_nodes)
            }
        }
    if algo == "bfs":
        return {"algorithm": "bfs", "features": features, "output": bfs(adj_list, 0)}
    elif algo == "dfs":
        return {"algorithm": "dfs", "features": features, "output": dfs(adj_list, 0)}
    elif detect_cycle:
        return {"algorithm": "cycle_detection", "features": features, "output": has_cycle(adj_list)}
    elif use_union_find:
        return {"algorithm": "union_find_cycle_check", "features": features, "output": run_union_cycle_check(adj_list, num_nodes)}
    elif use_topo_sort:
        return {"algorithm": "topological_sort", "features": features, "output": topo_sort(adj_list, num_nodes)}
    elif matrix:
        return {"algorithm": "dijkstra_matrix", "features": features, "output": dijkstra_matrix(adj_list, 0)}
    else:
        return {"algorithm": "dijkstra_heap", "features": features, "output": dijkstra_heap(adj_list, 0)}
def run_union_cycle_check(adj_list, n):
    uf = UnionFind(n)
    for u in adj_list:
        for v in adj_list[u]:
            if u < v:  
                if not uf.union(u, v):
                    return True
    return False
