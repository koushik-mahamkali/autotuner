# autograph.py
# Visualizer + Selector for AutoTuner graph algorithms

import os
from autotuner import graph_features, model_graph, autograph_logger
from autotuner.graphs import traversal, shortest_path, mst, topological, network_flow
from visualizers import plot_decision_graph, plot_graph_result
from autotuner.fallback import Fallback

# Mapping ML model's prediction to actual functions
graph_algorithm_map = {
    "bfs": traversal.bfs,
    "dfs": traversal.dfs,
    "dijkstra": shortest_path.dijkstra,
    "bellman_ford": shortest_path.bellman_ford,
    "kruskal": mst.kruskal,
    "prim": mst.prim,
    "topological_sort": topological.topological_sort,
    "ford_fulkerson": network_flow.ford_fulkerson,
    "edmonds_karp": network_flow.edmonds_karp,
    "dinic": network_flow.dinic,
}

def autograph(graph):
    feats = graph_features.extract_graph_features(graph)
    best_algo_name = model_graph.predict_graph(feats)
    selected_algo = graph_algorithm_map.get(best_algo_name)
    if selected_algo is None:
        result, best_algo_name = Fallback.graph_algorithm(graph)
        autograph_logger.log_graph_run(best_algo_name, 0)
        return result, best_algo_name
    import time
    start = time.time()
    result = selected_algo(graph)
    elapsed_time = (time.time() - start) * 1000  # ms

    autograph_logger.log_graph_run(best_algo_name, elapsed_time)
    
    # Optional visualization prompt
    if input("Visualize graph result? (y/n): ").lower() == 'y':
        plot_graph_result(graph, result, best_algo_name)
    if input("Visualize graph decision history? (y/n): ").lower() == 'y':
        plot_decision_graph(autograph_logger.get_graph_history())

    return result, best_algo_name