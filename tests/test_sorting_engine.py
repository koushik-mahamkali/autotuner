from autotuner_core.autotuner.switcher import choose_sort_algorithm

def test_quick_sort_selection():
    result = choose_sort_algorithm([9, 1, 4, 2])
    assert result["algorithm"] in {"quick_sort", "insertion_sort", "merge_sort"}
    assert result["sorted_array"] == sorted([9, 1, 4, 2])
