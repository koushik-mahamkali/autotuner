# 🔧 AutoTuner: Intelligent Algorithm Recommender

**AutoTuner** is a smart algorithm recommendation engine that analyzes input data (arrays or graphs) and selects the most efficient algorithm based on structural and statistical features. It is designed to assist developers, educators, and learners in choosing optimal algorithms without manual trial and error.

---

> ⚠️ **Note:** This is a **beta release of Version 1.0** intended for testing.  
> 🐞 Please report any bugs or provide feedback to help improve stability and performance.

---

## 🚀 Key Features

### 📊 Sorting Engine
Selects the most suitable sorting algorithm based on data features such as size, value range, and sortedness.

**Algorithms supported:**
- Insertion Sort  
- Merge Sort  
- Quick Sort  
- Counting Sort  
- TimSort  

---

### 🕸️ Graph Engine
Analyzes the graph's structure and properties to recommend ideal algorithms for traversal, shortest path, or cycle detection.

**Algorithms supported:**
- BFS  
- DFS  
- Dijkstra (Heap/Matrix)  
- Topological Sort  
- Cycle Detection  
- Union-Find Cycle Check  

**Graph features detected:**
- Directed/Undirected graphs  
- Weighted/Unweighted edges  
- Cycles  
- Density and connectivity  

---

### 💻 CLI Tools

- `autotuner-sort` — Recommends and runs the best sorting algorithm  
- `autotuner-graph` — Detects graph type and runs the most suitable graph algorithm  
- Accepts JSON input for graphs  
- Supports graph visualizations via `networkx` and `matplotlib`

---

## 📦 Installation

```bash
git clone https://github.com/koushik-mahamkali/autotuner
cd autotuner-engine
pip install -e .
```

---

## ⚙️ Usage Examples

### ✅ Sorting Example

```bash
autotuner-sort --input "[10, 3, 5, 1, 2]"
```

**Expected Output:**
```text
✅ Recommended Algorithm: Quick Sort
➡️ Sorted Output: [1, 2, 3, 5, 10]
```

---

### 🧠 Graph Analysis Example

Create a file named `graph.json` with the following content:

```json
{
  "directed": true,
  "weighted": false,
  "nodes": 4,
  "edges": [[0, 1], [1, 2], [2, 3]]
}
```

Then run:

```bash
autotuner-graph --input graph.json
```

**Expected Output (example):**
```text
🔍 Graph Analysis Complete
➡️ Detected: Directed, Unweighted, Acyclic
✅ Recommended Algorithm: Topological Sort
```

---

## 🧠 Behind the Scenes

AutoTuner uses a combination of feature extractors and rule-based heuristics to:
- Score array "sortedness"
- Detect graph density, direction, cycles, and edge weights
- Route the input to the optimal algorithm with explainability

---

## 📂 Project Structure

```text
autotuner/
├── autotuner/
│   ├── sort_engine.py
│   ├── graph_engine.py
│   ├── graph_features/
│   ├── sort_features/
│   ├── visualizers/
│   └── logger.py
├── cli/
│   ├── autotuner_sort.py
│   └── autotuner_graph.py
├── examples/
├── tests/
├── README.md
```

---

## 📊 Visualization

AutoTuner generates clean and interpretable graph visualizations using:
- `networkx`
- `matplotlib`

---

## ✅ Why Use AutoTuner?

- ⚙️ **Automation** — No need to guess; AutoTuner picks the best-fit algorithm  
- 📈 **Efficiency** — Decisions are based on key data features  
- 👨‍🏫 **Educational** — Understand why a specific algorithm fits your input  
- 🧩 **Extensible** — Add new algorithms or decision rules easily  

---

## 🤝 Contributing

Contributions are welcome!  
If you find bugs or want to enhance the engine, feel free to open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📬 Contact

**Krishna Koushik Mahamkali**  
📧 [LinkedIn](https://www.linkedin.com/in/monkeyknight/)  
📁 [GitHub Portfolio](https://github.com/koushik-mahamkali)
