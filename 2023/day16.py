# input_data = """.|...\\....
# |.-.\\.....
# .....|-...
# ........|.
# ..........
# .........\\
# ..../.\\\\..
# .-.-/..|..
# .|....-|.\\
# ..//.|...."""
from input_data import input_data


import sys

sys.setrecursionlimit(1500**2)


class Vector:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __add__(self, b):
        return Vector(self.y + b.y, self.x + b.x)

    def __str__(self):
        return str(f"{self.y}, {self.x}")


UP = Vector(-1, 0)
DOWN = Vector(1, 0)
RIGHT = Vector(0, 1)
LEFT = Vector(0, -1)


def make_map(input_data):
    matrix = []
    for line in input_data.splitlines():
        new_line = []
        for c in line:
            new_line.append(c)
        matrix.append(new_line)
    return matrix


def make_blank_matrix(input_data):
    matrix = []
    for line in input_data.splitlines():
        new_line = []
        for c in line:
            new_line.append(".")
        matrix.append(new_line)
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print("".join(line))


def mark_location(location):
    global result
    result[location.y][location.x] = "#"


result = make_blank_matrix(input_data)
print_matrix(result)

print("Executing")


# mark_location(result, actual_location)
history = set()


def evaluate_position(map, position, direction):
    global result, history

    if ((position.y, position.x), (direction.y, direction.x)) in history:
        return

    history.add(((position.y, position.x), (direction.y, direction.x)))

    if not (0 <= position.y < len(map)):
        return

    if not (0 <= position.x < len(map[0])):
        return

    char = map[position.y][position.x]
    mark_location(position)

    # print(position, direction)
    # print_matrix(result)
    # input()

    if char == ".":
        evaluate_position(map, position + direction, direction)
    elif char == "-":
        if direction == RIGHT:
            evaluate_position(map, position + RIGHT, RIGHT)
        elif direction == LEFT:
            evaluate_position(map, position + LEFT, LEFT)
        elif direction == UP or direction == DOWN:
            evaluate_position(map, position + RIGHT, RIGHT)
            evaluate_position(map, position + LEFT, LEFT)
    elif char == "|":
        if direction == UP:
            evaluate_position(map, position + UP, UP)
        elif direction == DOWN:
            evaluate_position(map, position + DOWN, DOWN)
        elif direction == LEFT or direction == RIGHT:
            evaluate_position(map, position + UP, UP)
            evaluate_position(map, position + DOWN, DOWN)
    elif char == "\\":
        if direction == RIGHT:
            evaluate_position(map, position + DOWN, DOWN)
        elif direction == LEFT:
            evaluate_position(map, position + UP, UP)
        elif direction == UP:
            evaluate_position(map, position + LEFT, LEFT)
        elif direction == DOWN:
            evaluate_position(map, position + RIGHT, RIGHT)
    elif char == "/":
        if direction == RIGHT:
            evaluate_position(map, position + UP, UP)
        elif direction == LEFT:
            evaluate_position(map, position + DOWN, DOWN)
        elif direction == UP:
            evaluate_position(map, position + RIGHT, RIGHT)
        elif direction == DOWN:
            evaluate_position(map, position + LEFT, LEFT)


mapp = make_map(input_data)
# part 1
# evaluate_position(mapp, Vector(0, 0), RIGHT)
# print_matrix(result)

# count_hash = 0
# for line in result:
#     for char in line:
#         if char == "#":
#             count_hash += 1
# print(count_hash)

# part 2


def count_energy(result):
    count_hash = 0
    for line in result:
        for char in line:
            if char == "#":
                count_hash += 1
    return count_hash


max_energy = 0
# up
for x in range(len(mapp[0])):
    result = make_blank_matrix(input_data)
    history = set()
    evaluate_position(mapp, Vector(0, x), DOWN)
    e = count_energy(result)
    if e > max_energy:
        max_energy = e

# down
for x in range(len(mapp[-1])):
    result = make_blank_matrix(input_data)
    history = set()
    evaluate_position(mapp, Vector(len(mapp) - 1, x), UP)
    e = count_energy(result)
    if e > max_energy:
        max_energy = e

# right
for y in range(len(mapp)):
    result = make_blank_matrix(input_data)
    history = set()
    evaluate_position(mapp, Vector(y, 0), RIGHT)
    e = count_energy(result)
    if e > max_energy:
        max_energy = e

# left
for y in range(len(mapp)):
    result = make_blank_matrix(input_data)
    history = set()
    evaluate_position(mapp, Vector(y, len(mapp[0]) - 1), LEFT)
    e = count_energy(result)
    if e > max_energy:
        max_energy = e

print(max_energy)
