import numpy as np
from scipy.stats import kurtosis,skew
def enhanced_features(arr):
    arr = np.array(arr)

    if len(arr) == 0:
        return [0] * 18

    is_integer = int(np.all(np.equal(np.mod(arr, 1), 0)))
    is_small_range = int(np.ptp(arr) < 1000)
    duplicate_ratio = 1 - len(set(arr)) / len(arr)
    is_sorted = int(np.all(arr[:-1] <= arr[1:]))
    is_reversed = int(np.all(arr[:-1] >= arr[1:]))

    return [
        len(arr),                                # 1. Size
        np.mean(arr),                            # 2. Mean
        np.std(arr),                             # 3. Std dev
        len(set(arr)) / len(arr),                # 4. Uniqueness ratio
        np.count_nonzero(np.diff(arr) < 0) / len(arr),  # 5. Unsortedness
        np.max(arr) - np.min(arr),               # 6. Range
        skew(arr),                               # 7. Skewness
        kurtosis(arr),                           # 8. Kurtosis
        np.percentile(arr, 25),                  # 9. Q1
        np.percentile(arr, 75),                  # 10. Q3
        is_sorted,                               # 11. Already sorted
        is_reversed,                             # 12. Reverse sorted
        duplicate_ratio,                         # 13. Duplicates ratio
        np.median(np.diff(np.sort(arr))),        # 14. Gap uniformity
        is_integer,                              # 15. Integer-only (good for Counting/Radix)
        is_small_range,                          # 16. Small integer range
        np.sum(arr == arr[0]) / len(arr),        # 17. Uniformity
        len(np.unique(np.floor(arr))) / len(arr) # 18. Distribution spread
    ]