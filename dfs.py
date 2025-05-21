
from cube import Cube

VALID_MOVES = ['U', 'Ui', 'U2', 'D', 'Di', 'D2', 'F', 'Fi', 'F2',
               'B', 'Bi', 'B2', 'L', 'Li', 'L2', 'R', 'Ri', 'R2']

def dfs(start_cube, max_depth=6):
    path = []

    def dfs_recursive(cube, depth, last_move=None):
        if cube.is_solved():
            return True
        
        if depth == 0:
            return False

        for move in VALID_MOVES:
            # Avoid doing a move that just undoes the last one (simple pruning)
            if last_move and move[0] == last_move[0] and move != last_move:
                continue

            new_cube = cube.copy()
            new_cube.move(move)
            path.append(move)

            if dfs_recursive(new_cube, depth - 1, move):
                return True

            path.pop()

        return False

    if dfs_recursive(start_cube, max_depth):
        return path
    else:
        return None