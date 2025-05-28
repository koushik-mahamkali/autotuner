# visualizers.py

import matplotlib.pyplot as plt
import seaborn as sns
import os
import networkx as nx

# --- SORT VISUALIZATIONS ---

def plot_sort_array(before, after, algorithm_name, save_path=None):
    sns.set_theme(style="white")
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    sns.barplot(x=list(range(len(before))), y=before, color="skyblue")
    plt.title("Original Array")

    plt.subplot(1, 2, 2)
    sns.barplot(x=list(range(len(after))), y=after, color="limegreen")
    plt.title(f"Sorted Array ({algorithm_name})")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    plt.tight_layout()
    plt.show()


def plot_decision_sort(history, save_path=None):
    if not history:
        print("No history to plot.")
        return

    sns.set_theme(style="whitegrid")
    algorithms = [entry['algorithm'] for entry in history]
    times = [entry['execution_time_ms'] for entry in history]
    runs = list(range(len(history)))

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=runs, y=times, hue=algorithms, marker='o', palette="tab10")
    plt.title("AutoTuner Sort Decisions Over Time")
    plt.xlabel("Run")
    plt.ylabel("Execution Time (ms)")
    plt.legend(title="Algorithm")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()

# --- GRAPH VISUALIZATIONS ---

def plot_graph_result(graph, result, algorithm_name, save_path=None):
    """
    Visualizes the graph structure and highlights the result (e.g., path or tree)
    """
    G = nx.Graph()

    for u in graph['nodes']:
        G.add_node(u)

    for u, v, w in graph['edges']:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=10, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w for u, v, w in graph['edges']})

    if isinstance(result, list):
        path_edges = list(zip(result, result[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3)

    plt.title(f"Graph Result: {algorithm_name}")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)

    plt.show()


def plot_decision_graph(history, save_path=None):
    if not history:
        print("No history to plot.")
        return

    sns.set(style="whitegrid")
    algorithms = [entry['algorithm'] for entry in history]
    performance = [entry['execution_time_ms'] for entry in history]
    timestamps = list(range(len(history)))

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=timestamps, y=performance, hue=algorithms, palette="tab10", marker='o')
    plt.title("AutoTuner Graph Algorithm Decisions Over Time")
    plt.xlabel("Run")
    plt.ylabel("Execution Time (ms)")
    plt.legend(title="Algorithm")

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path)
    plt.show()
