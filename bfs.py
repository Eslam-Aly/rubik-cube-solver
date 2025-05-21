# bfs_solver.py

from cube import Cube
from collections import deque

VALID_MOVES = ['U', 'Ui', 'U2', 'D', 'Di', 'D2',
               'F', 'Fi', 'F2', 'B', 'Bi', 'B2',
               'L', 'Li', 'L2', 'R', 'Ri', 'R2']

def bfs(start_cube, max_depth=6):
    visited = set()
    queue = deque()
    
    # Store: (cube, path, depth)
    queue.append((start_cube, [], 0))

    while queue:
        cube, path, depth = queue.popleft()

        # Check if solved
        if cube.is_solved():
            return path

        if depth >= max_depth:
            continue

        # Convert cube to hashable state
        cube_hash = hash(cube)
        if cube_hash in visited:
            continue

        visited.add(cube_hash)

        for move in VALID_MOVES:
            # Avoid immediately undoing the last move
            if path and move[0] == path[-1][0] and move != path[-1]:
                continue

            new_cube = cube.copy()
            new_cube.move(move)
            new_path = path + [move]
            queue.append((new_cube, new_path, depth + 1))

    return None  # No solution found within depth limit