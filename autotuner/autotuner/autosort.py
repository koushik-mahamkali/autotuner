# autosort.py

import time
from autotuner import features, model
from autotuner.algorithms import classic, counting_based, external, hybrid, niche
from autotuner.autosort_logger import autosort_logger
from autotuner.visualizers import plot_decision_sort, plot_sort_array
from autotuner.fallback import Fallback

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

def autosort(arr, visualize=False):
    feats = features.extract_features(arr)
    best_algo_name = model.predict(feats)
    sort_func = algorithm_map.get(best_algo_name)
    if sort_func is None:
        sorted_arr, best_algo_name = Fallback.sort(arr)
        autosort_logger.log(arr, best_algo_name, 0)
        return sorted_arr, best_algo_name
    start = time.time()
    sorted_arr = sort_func(arr.copy())
    elapsed_ms = (time.time() - start) * 1000

    autosort_logger.log(arr, best_algo_name, elapsed_ms)

    if visualize:
        plot_sort_array(arr, sorted_arr, best_algo_name)

    return sorted_arr, best_algo_name

def visualize_autosort_history():
    logs = autosort_logger.get_logs()
    if logs:
        history = [(entry["selected_algorithm"], entry["execution_time_ms"]) for entry in logs]
        plot_decision_sort(history)
    else:
        print("No logs available for visualization.")
