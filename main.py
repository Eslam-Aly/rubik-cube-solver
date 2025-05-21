# main.py

from cube import Cube
from dfs import dfs
from bfs import bfs
from astar import astar

cube = Cube()

# Scramble the cube with a few moves
scramble_moves = ['F', 'R', 'Ui']
for move in scramble_moves:
    cube.move(move)

print("Scramble:", scramble_moves)
print("Is Solved?", cube.is_solved())

# Try DFS
solution_dfs = dfs(cube, max_depth=6)
print("DFS solution:", solution_dfs)

# Try BFS
solution_bfs = bfs(cube, max_depth=6)
print("BFS solution:", solution_bfs)

# Try A* Search
solution_astar = astar(cube, max_depth=12)
print("A* solution:", solution_astar)