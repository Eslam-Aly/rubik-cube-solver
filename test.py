import time
import random
import tracemalloc
import csv

from cube import Cube
from dfs import dfs
from bfs import bfs
from astar import astar

VALID_MOVES = ['U', 'Ui', 'U2', 'D', 'Di', 'D2',
               'F', 'Fi', 'F2', 'B', 'Bi', 'B2',
               'L', 'Li', 'L2', 'R', 'Ri', 'R2']

def scramble(cube, moves_count=3):
    """Applies random moves to scramble the cube."""
    scramble_moves = random.choices(VALID_MOVES, k=moves_count)
    for move in scramble_moves:
        cube.move(move)
    return scramble_moves

def test_solver(name, algorithm, cube, max_depth):
    """Times and measures memory used by a solver algorithm."""
    tracemalloc.start()
    start_time = time.time()

    solution = algorithm(cube, max_depth=max_depth)

    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    duration = end_time - start_time
    return {
        'name': name,
        'moves': solution,
        'time_sec': round(duration, 4),
        'memory_kb': round(peak / 1024, 2)
    }

def run_all_tests(repeats=100):
    """Runs tests across cube sizes and solvers, exports results to CSV."""
    all_results = []

    for size in range(2, 7):  # 2x2x2 to 6x6x6
        print(f"\nTesting {size}x{size}x{size} Cube...")

        for name, algo, depth in [
            ("DFS", dfs, 6),
            ("BFS", bfs, 6),
            ("A*", astar, 12)
        ]:
            total_time = 0
            total_memory = 0
            total_moves = 0
            success_runs = 0

            for i in range(repeats):
                cube = Cube(size)
                scramble_moves = scramble(cube, moves_count=3)
                result = test_solver(name, algo, cube.copy(), depth)

                if result['moves']:
                    success_runs += 1
                    total_time += result['time_sec']
                    total_memory += result['memory_kb']
                    total_moves += len(result['moves'])

                # Optional: show progress
                if (i + 1) % 10 == 0:
                    print(f"  {name} - {i+1}/{repeats} runs complete...")

            if success_runs > 0:
                avg_time = total_time / success_runs
                avg_memory = total_memory / success_runs
                avg_moves = total_moves / success_runs
            else:
                avg_time = avg_memory = avg_moves = 0

            all_results.append({
                'cube_size': f"{size}x{size}x{size}",
                'algorithm': name,
                'avg_time_sec': round(avg_time, 4),
                'avg_memory_kb': round(avg_memory, 2),
                'avg_move_count': int(avg_moves),
                'success_runs': success_runs,
                'total_runs': repeats
            })

    # Export to CSV
    with open('solver_results_avg.csv', 'w', newline='') as csvfile:
        fieldnames = ['cube_size', 'algorithm', 'avg_time_sec', 'avg_memory_kb', 'avg_move_count', 'success_runs', 'total_runs']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)

    print("\nAll tests complete. Results exported to solver_results_avg.csv")

# Run the test
if __name__ == "__main__":
    run_all_tests(repeats=100)