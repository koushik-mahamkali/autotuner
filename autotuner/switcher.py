from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.quick_sort import quick_sort  # ✅ Add this
from autotuner.features import get_array_features
from algorithms.sorting.timsort import timsort
from algorithms.sorting.counting_sort import counting_sort
def choose_sort_algorithm(arr):
    features = get_array_features(arr)
    size = features["size"]
    sortedness = features["sortedness_score"]
    if size <= 10:
        chosen_algo = "insertion_sort"
        sorted_arr = insertion_sort(arr)
    elif sortedness > 0.85:
        chosen_algo = "timsort"
        sorted_arr = timsort(arr)
    elif all(isinstance(x, int) for x in arr) and min(arr) >= 0 and max(arr) < 10_000:
        chosen_algo = "counting_sort"
        sorted_arr = counting_sort(arr)
    elif 10 < size <= 30:
        chosen_algo = "quick_sort"
        sorted_arr = quick_sort(arr)
    else:
        chosen_algo = "merge_sort"
        sorted_arr = merge_sort(arr)
    return {
        "sorted_array": sorted_arr,
        "algorithm": chosen_algo,
        "features": features
    }
