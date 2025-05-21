# heuristics.py

def misplaced_heuristic(cube):
    faces = cube.faces
    size = cube.size
    count = 0

    for face in faces:
        center = faces[face][size // 2][size // 2]
        for row in faces[face]:
            for color in row:
                if color != center:
                    count += 1

    # Roughly divide by 8 (each move may fix multiple facelets)
    return count // 8