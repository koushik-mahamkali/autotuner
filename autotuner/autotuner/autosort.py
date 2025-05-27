# autosort_viz.py
# Visualizer + Selector for AutoTuner sorting algorithms

import matplotlib.pyplot as plt
import seaborn as sns
import os
import random

# --- SORT SELECTION MODULE ---
from autotuner import features, model
from autotuner.algorithms import classic, counting_based, external, hybrid, niche

algorithm_map = {
    "insertion_sort": classic.insertion_sort,
    "merge_sort": classic.merge_sort,
    "heap_sort": classic.heap_sort,
    "counting_sort": counting_based.counting_sort,
    "radix_sort": counting_based.radix_sort,
    "bucket_sort": counting_based.bucket_sort,
    "cycle_sort": counting_based.cycle_sort,
    "flash_sort": counting_based.flash_sort,
    "external_sort": external.external_merge_sort,
    "tim_sort": hybrid.tim_sort,
    "intro_sort": hybrid.intro_sort,
    "smart_sort": hybrid.smart_sort,
    "is_nearly_sorted": hybrid.is_nearly_sorted,
    "binary_insertion_sort": hybrid.binary_insertion_sort,
    "bitonic_sort": niche.bitonic_sort,
    "tree_sort": niche.tree_sort,
    "odd_even_sort": niche.odd_even_sort,
    "shell_sort": niche.shell_sort,
}

def autosort(arr):
    feats = features.extract_features(arr)
    best_algo_name = model.predict(feats)
    selected_algo = algorithm_map.get(best_algo_name, hybrid.tim_sort)
    sorted_arr = selected_algo(arr.copy())
    return sorted_arr, best_algo_name

# --- VISUALIZATION MODULE ---

def plot_decision_sort(history, save_path=None):
    """
    Plots algorithm choices over multiple runs
    :param history: List of tuples [(algorithm_name, time_taken, timestamp), ...]
    """
    if not history:
        print("No history to plot.")
        return

    sns.set_theme(style="whitegrid")
    algorithms = [entry[0] for entry in history]
    times = [entry[1] for entry in history]
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

def plot_sort_array(before, after, algorithm_name, save_path=None):
    """
    Visualizes the array before and after sorting
    """
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

# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    history = []
    for _ in range(5):
        arr = random.sample(range(1, 100), 30)
        sorted_arr, algo = autosort(arr)
        import time
        start = time.time()
        algorithm_map[algo](arr.copy())
        elapsed = (time.time() - start) * 1000  # ms

        history.append((algo, elapsed))

        print(f"Algorithm Used: {algo}")
        plot_sort_array(arr, sorted_arr, algo)

    plot_decision_sort(history)
