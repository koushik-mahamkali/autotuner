# autograph.py
# Visualizer + Selector for AutoTuner graph algorithms

import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- GRAPH SELECTION MODULE ---
from autotuner import graph_features,model_graph
from autotuner.graphs import traversal, shortest_path, mst, topological, network_flow

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
        raise ValueError("No matching algorithm found for: {}".format(best_algo_name))

    result = selected_algo(graph)
    return result, best_algo_name

# --- VISUALIZATION MODULE ---
def plot_decision_graph(history, save_path=None):
    """
    Plots which algorithm was chosen over multiple runs
    :param history: List of tuples [(algorithm_name, accuracy/performance, timestamp), ...]
    :param save_path: Path to save the plot
    """
    if not history:
        print("No history to plot.")
        return

    sns.set_theme(style="whitegrid")
    algorithms = [entry[0] for entry in history]
    performance = [entry[1] for entry in history]
    timestamps = list(range(len(history)))

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=timestamps, y=performance, hue=algorithms, palette="tab10", marker='o')
    plt.title("AutoTuner Algorithm Decisions Over Time")
    plt.xlabel("Run")
    plt.ylabel("Performance Metric (lower is better)")
    plt.legend(title="Algorithm")
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

def plot_feature_importance(importances, feature_names, save_path=None):
    """
    Plots feature importance from the ML model (if using one)
    :param importances: List of importance scores
    :param feature_names: List of feature names
    :param save_path: Path to save the plot
    """
    if not importances:
        print("No importances to plot.")
        return

    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(10, 6))
    sorted_idx = sorted(range(len(importances)), key=lambda k: importances[k], reverse=True)
    sorted_names = [feature_names[i] for i in sorted_idx]
    sorted_importances = [importances[i] for i in sorted_idx]

    sns.barplot(x=sorted_importances, y=sorted_names, palette="viridis")
    plt.title("Feature Importance in Algorithm Selection")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()
