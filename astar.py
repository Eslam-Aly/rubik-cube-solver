# astar_solver.py

from cube import Cube
from heuristics import misplaced_heuristic
import heapq

VALID_MOVES = ['U', 'Ui', 'U2', 'D', 'Di', 'D2',
               'F', 'Fi', 'F2', 'B', 'Bi', 'B2',
               'L', 'Li', 'L2', 'R', 'Ri', 'R2']

def astar(start_cube, max_depth=12):
    open_heap = []
    closed_set = set()

    # (f, g, cube, path)
    g = 0
    h = misplaced_heuristic(start_cube)
    heapq.heappush(open_heap, (g + h, g, start_cube, []))

    while open_heap:
        f_score, g_score, cube, path = heapq.heappop(open_heap)

        if cube.is_solved():
            return path

        cube_hash = hash(cube)
        if cube_hash in closed_set:
            continue
        closed_set.add(cube_hash)

        if g_score >= max_depth:
            continue

        for move in VALID_MOVES:
            if path and move[0] == path[-1][0] and move != path[-1]:
                continue

            new_cube = cube.copy()
            new_cube.move(move)
            new_path = path + [move]

            g_new = g_score + 1
            h_new = misplaced_heuristic(new_cube)
            f_new = g_new + h_new

            heapq.heappush(open_heap, (f_new, g_new, new_cube, new_path))

    return None