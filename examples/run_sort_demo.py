import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from autotuner.switcher import choose_sort_algorithm
from autotuner.benchmark import benchmark
from autotuner.logger import init_logger, log_run
from autotuner.visualizer import plot_runtime_vs_size, plot_algorithm_distribution
def main():
    import random
    test_cases = [
        random.sample(range(100), 5),   # small, random
        sorted(random.sample(range(100), 10)),  # sorted
        random.sample(range(100), 15),  # medium random
        list(range(30, 0, -1)),         # reverse sorted
        random.sample(range(100), 50),  # larger
        random.sample(range(10), 8),    # nearly sorted
        [1, 2, 3, 4, 5, 6, 6, 6, 7, 8], # duplicate heavy
    ]
    for arr in test_cases:
        result, time_taken = benchmark(choose_sort_algorithm, arr)
        log_run(result["algorithm"], result["features"], time_taken)
        print("🔹 Input:", arr)
        print("🔹 Algo :", result["algorithm"])
        print("🔹 Time :", time_taken)
        print("-" * 30)
    init_logger()
    result, time_taken = benchmark(choose_sort_algorithm, arr)
    log_run(result["algorithm"], result["features"], time_taken)
    print("\n AutoTuner Decision Summary")
    print("-" * 35)
    print("Original Array      :", arr)
    print("Sorted Array        :", result["sorted_array"])
    print("Algorithm Used      :", result["algorithm"])
    print("Input Features      :", result["features"])
    print("Execution Time (ms) :", time_taken)
if __name__ == "__main__":
    main()
    plot_runtime_vs_size()
    plot_algorithm_distribution()


