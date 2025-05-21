# main.py

from cube import Cube
from dfs import dfs

cube = Cube()

# Scramble the cube with a few moves
scramble_moves = ['F', 'R', 'Ui']
for move in scramble_moves:
    cube.move(move)

print("Scramble:", scramble_moves)
print("Is Solved?", cube.is_solved())

# Try solving with DFS (max depth = 6)
solution = dfs(cube, max_depth=6)

if solution:
    print("Solution found:", solution)
else:
    print("No solution found within depth limit")