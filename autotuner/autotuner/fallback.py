# fallback.py

from autotuner.algorithms import hybrid
from autotuner.graphs import traversal

class Fallback:
    @staticmethod
    def sort(arr):
        """
        Fallback sorting using tim_sort (robust and efficient).
        """
        print("[Fallback] Using tim_sort as default sorting algorithm.")
        return hybrid.tim_sort(arr.copy()), "tim_sort"

    @staticmethod
    def graph_algorithm(graph):
        """
        Fallback graph algorithm using BFS (works for most use-cases).
        """
        print("[Fallback] Using bfs as default graph algorithm.")
        return traversal.bfs(graph), "bfs"
