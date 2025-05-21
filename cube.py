# cube.py

import copy

class Cube:
    def __init__(self, size=3):
        self.size = size
        self.faces = {
            'U': [[ 'W' for _ in range(size)] for _ in range(size)],
            'R': [[ 'R' for _ in range(size)] for _ in range(size)],
            'F': [[ 'G' for _ in range(size)] for _ in range(size)],
            'D': [[ 'Y' for _ in range(size)] for _ in range(size)],
            'L': [[ 'O' for _ in range(size)] for _ in range(size)],
            'B': [[ 'B' for _ in range(size)] for _ in range(size)],
        }

    def copy(self):
        # Create a deep copy to avoid shared references
        new_cube = Cube(self.size)
        new_cube.faces = copy.deepcopy(self.faces)
        return new_cube

    def is_solved(self):
        # Check if all stickers on each face match the center color
        for face in self.faces:
            center_color = self.faces[face][self.size // 2][self.size // 2]
            for row in self.faces[face]:
                if any(cell != center_color for cell in row):
                    return False
        return True

    def move(self, move_str):
        # Placeholder for move parser
        # Example: 'U', 'Ui', 'U2'
        direction = 'cw'  # clockwise
        times = 1

        if move_str.endswith('i'):
            direction = 'ccw'
        elif move_str.endswith('2'):
            times = 2

        face = move_str[0]

        for _ in range(times):
            self._rotate(face, direction)

    def _rotate(self, face, direction):
        self._rotate_face(face, direction)
        self._rotate_edges(face, direction)

    def _rotate_face(self, face, direction):
        # Rotate the face itself (just the matrix)
        matrix = self.faces[face]
        if direction == 'cw':
            self.faces[face] = [list(row) for row in zip(*matrix[::-1])]
        elif direction == 'ccw':
            self.faces[face] = [list(row) for row in zip(*matrix)][::-1]

    def _rotate_edges(self, face, direction):
        s = self.size
        f = self.faces

        if face == 'U':
            top_f = f['F'][0][:]
            top_r = f['R'][0][:]
            top_b = f['B'][0][:]
            top_l = f['L'][0][:]

            if direction == 'cw':
                f['F'][0] = top_l
                f['R'][0] = top_f
                f['B'][0] = top_r
                f['L'][0] = top_b
            elif direction == 'ccw':
                f['F'][0] = top_r
                f['R'][0] = top_b
                f['B'][0] = top_l
                f['L'][0] = top_f

        elif face == 'D':
            bot_f = f['F'][-1][:]
            bot_l = f['L'][-1][:]
            bot_b = f['B'][-1][:]
            bot_r = f['R'][-1][:]

            if direction == 'cw':
                f['F'][-1] = bot_r
                f['L'][-1] = bot_f
                f['B'][-1] = bot_l
                f['R'][-1] = bot_b
            elif direction == 'ccw':
                f['F'][-1] = bot_l
                f['L'][-1] = bot_b
                f['B'][-1] = bot_r
                f['R'][-1] = bot_f

        elif face == 'F':
            bot_u = f['U'][-1][:]
            left_r = [f['R'][i][0] for i in range(s)]
            top_d = f['D'][0][:]
            right_l = [f['L'][i][-1] for i in range(s)]

            if direction == 'cw':
                f['U'][-1] = right_l[::-1]
                for i in range(s):
                    f['R'][i][0] = bot_u[i]
                f['D'][0] = left_r[::-1]
                for i in range(s):
                    f['L'][i][-1] = top_d[i]
            elif direction == 'ccw':
                f['U'][-1] = left_r
                for i in range(s):
                    f['R'][i][0] = top_d[::-1][i]
                f['D'][0] = right_l
                for i in range(s):
                    f['L'][i][-1] = bot_u[::-1][i]

        elif face == 'B':
            top_u = f['U'][0][:]
            left_l = [f['L'][i][0] for i in range(s)]
            bottom_d = f['D'][-1][:]
            right_r = [f['R'][i][-1] for i in range(s)]

            if direction == 'cw':
                f['U'][0] = left_l[::-1]
                for i in range(s):
                    f['L'][i][0] = bottom_d[i]
                f['D'][-1] = right_r[::-1]
                for i in range(s):
                    f['R'][i][-1] = top_u[i]
            elif direction == 'ccw':
                f['U'][0] = right_r
                for i in range(s):
                    f['L'][i][0] = top_u[::-1][i]
                f['D'][-1] = left_l
                for i in range(s):
                    f['R'][i][-1] = bottom_d[::-1][i]

        elif face == 'L':
            col_u = [f['U'][i][0] for i in range(s)]
            col_f = [f['F'][i][0] for i in range(s)]
            col_d = [f['D'][i][0] for i in range(s)]
            col_b = [f['B'][s - 1 - i][-1] for i in range(s)]  # reverse column from B

            if direction == 'cw':
                for i in range(s):
                    f['U'][i][0] = col_b[i]
                    f['F'][i][0] = col_u[i]
                    f['D'][i][0] = col_f[i]
                    f['B'][s - 1 - i][-1] = col_d[i]
            elif direction == 'ccw':
                for i in range(s):
                    f['U'][i][0] = col_f[i]
                    f['F'][i][0] = col_d[i]
                    f['D'][i][0] = col_b[i]
                    f['B'][s - 1 - i][-1] = col_u[i]

        elif face == 'R':
            col_u = [f['U'][i][-1] for i in range(s)]
            col_f = [f['F'][i][-1] for i in range(s)]
            col_d = [f['D'][i][-1] for i in range(s)]
            col_b = [f['B'][s - 1 - i][0] for i in range(s)]  # reverse column from B

            if direction == 'cw':
                for i in range(s):
                    f['U'][i][-1] = col_f[i]
                    f['F'][i][-1] = col_d[i]
                    f['D'][i][-1] = col_b[i]
                    f['B'][s - 1 - i][0] = col_u[i]
            elif direction == 'ccw':
                for i in range(s):
                    f['U'][i][-1] = col_b[i]
                    f['F'][i][-1] = col_u[i]
                    f['D'][i][-1] = col_f[i]
                    f['B'][s - 1 - i][0] = col_d[i]



    def __str__(self):
        # Simple string representation of the cube
        return '\n'.join(f"{face}:\n" + '\n'.join(str(row) for row in self.faces[face]) for face in self.faces)


    def __lt__(self, other):
        return True  # or False — doesn't matter, just avoids comparison crash

    def __eq__(self, other):
        return self.faces == other.faces

    def __hash__(self):
        return hash(tuple(
            tuple(tuple(row) for row in self.faces[face])
            for face in ['U', 'R', 'F', 'D', 'L', 'B']
        ))