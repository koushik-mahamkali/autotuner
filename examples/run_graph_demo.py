import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from autotuner.graph_switcher import choose_graph_algorithm
from autotuner.benchmark import benchmark
from autotuner.logger import init_graph_logger, log_graph_run
from autotuner.visualizer import (
    plot_graph_runtime_vs_nodes,
    plot_graph_algo_distribution,
    visualize_graph
)
from autotuner.graph_features import get_graph_features
def main():
    adj_list = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (3, 2)],
    2: [(0, 1), (3, 5)],
    3: [(1, 2), (2, 5), (4, 1)],
    4: [(3, 1), (5, 3)],
    5: [(4, 3)]
    }
    print(" Graph Input:", adj_list)
    features = get_graph_features(adj_list)
    print("Extracted Features:", features)
    init_graph_logger()
    result, time_taken = benchmark(choose_graph_algorithm, adj_list)
    log_graph_run(result["algorithm"], result["features"], time_taken)
    print("\n AutoTuner Graph Decision Summary")
    print("-" * 35)
    print("Algorithm Used      :", result["algorithm"])
    print("Output              :", result["output"])
    print("Features            :", result["features"])
    print("Execution Time (ms) :", time_taken)
    visualize_graph(adj_list,title="Dijkstra Graph View")
    plot_graph_runtime_vs_nodes()
    plot_graph_algo_distribution()
if __name__ == "__main__":
    main()
