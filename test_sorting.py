from autotuner.benchmark import benchmark
from autotuner.switcher import choose_sort_algorithm

arr = [5, 2, 4, 1]
result, time_taken = benchmark(choose_sort_algorithm, arr)

print(f"Used: {result['algorithm']}")
print(f"Time: {time_taken} ms")
print(f"Sorted: {result['sorted_array']}")
