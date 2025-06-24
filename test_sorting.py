from autotuner_core.autotuner.graph_switcher import choose_graph_algorithm

# Test Cases
test_cases = {
    "Weighted Sparse": {
        0: [(1, 4), (2, 1)],
        1: [(3, 2)],
        2: [(3, 5)],
        3: [(4, 1)],
        4: [(5, 3)],
        5: []
    },
    "Weighted Dense": {
        0: [(1, 1), (2, 1), (3, 1)],
        1: [(2, 1), (3, 1), (4, 1)],
        2: [(3, 1), (4, 1), (5, 1)],
        3: [(4, 1), (5, 1)],
        4: [(5, 1)],
        5: []
    },
    "DAG": {
        0: [1, 2],
        1: [3],
        2: [3],
        3: [4],
        4: []
    },
    "Dense Graph": {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    },
    "Sparse Graph": {
        0: [1],
        1: [2],
        2: [3],
        3: [4],
        4: []
    },
    "Cycle Graph": {
        0: [1],
        1: [2],
        2: [3],
        3: [1]
    },
    "Union-Find Cycle": {
        0: [1],
        1: [0, 2],
        2: [1, 3],
        3: [2, 0]
    },
    "Fully Connected": {
        0: [1, 2, 3],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [0, 1, 2]
    },
    "Tree": {
        0: [1, 2],
        1: [3, 4],
        2: [],
        3: [],
        4: []
    },
    "Empty": {}
}

print("\n\n===== AutoTuner Graph Algorithm Test Results =====")
for name, adj in test_cases.items():
    try:
        result = choose_graph_algorithm(adj)
        print(f"\n📌 Test Case: {name}")
        print(f"Algorithm: {result['algorithm']}")
        print(f"Output: {result['output']}")
    except Exception as e:
        print(f"\n❌ Test Case Failed: {name} - Error: {e}")
