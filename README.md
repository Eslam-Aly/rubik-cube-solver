# Rubik's Cube Solver: Algorithmic Comparison

This project presents a structured comparison of three classical search strategies for solving the Rubik’s Cube problem across varying cube sizes:

- Depth-First Search (DFS)  
- Breadth-First Search (BFS)  
- A* Search (A*)

The goal is to solve randomly scrambled Rubik’s Cubes ranging from **2×2×2** to **6×6×6** using algorithmic search. This project emphasizes a fair comparison under uniform initial conditions and repeated trials to measure performance across several metrics.

---

## 🎯 Objectives

- Evaluate the efficiency and performance of different search algorithms on Rubik’s Cubes.
- Benchmark performance across cube sizes: **2×2×2, 3×3×3, 4×4×4, 5×5×5, 6×6×6**
- Log and compare:
  - Success Rate  
  - Runtime  
  - Memory Usage  
  - Solution Length (Number of Moves)  

---

## 📁 Project Structure

<pre><code>
├── astar.py               # A* algorithm with heuristic
├── bfs.py                 # BFS implementation
├── cube.py                # Cube object representation and logic
├── dfs.py                 # DFS implementation
├── heuristics.py          # Heuristic functions used by A*
├── main.py                # Entry point for manual solving and testing
├── solver.py              # Handles multiple algorithm execution
├── test.py                # Benchmark runner and CSV logging
├── solver_results_avg.csv # Output: averaged results from all runs
├── .gitignore             # Git ignored files
├── LICENSE                # Project license (Apache 2.0)
└── README.md              # Project description (this file)
</code></pre>

---

## 🧪 Benchmarking Method

Each solver is evaluated on 100 randomly generated scramble states per cube size.  
All tests are performed under consistent conditions to ensure fairness.

**Metrics Recorded:**
- Total Solve Time  
- Peak Memory Usage  
- Number of Moves to Solution  
- Success/Failure Rate  

Results are stored in `solver_results_avg.csv` for analysis.

---

## 📝 License

This project is released under the **Apache-2.0 License**.

---

## 🤝 Contributing

Feel free to fork, modify, or improve the project. Pull requests are welcome!

---

## 👤 Author

Built by [Eslam Aly](https://github.com/Eslam-Aly) — exploring AI, search algorithms, and puzzle-solving.
