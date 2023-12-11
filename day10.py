from input_data import input_data
# input_data = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""

DOWN = (1,0)
UP = (-1,0)
LEFT = (0,-1)
RIGHT = (0,1)

# y, x
directions = {
    "|": ((DOWN, UP), (UP, DOWN)),
    "-": ((LEFT, RIGHT), (RIGHT, LEFT)),
    "L": ((DOWN, RIGHT), (LEFT, UP)),
    "J": ((DOWN, LEFT), (RIGHT, UP)),
    "7": ((UP, LEFT), (RIGHT, DOWN)),
    "F": ((LEFT, DOWN), (UP, RIGHT)),
    "S": ((DOWN, UP), (UP, DOWN), (LEFT, RIGHT), (RIGHT, LEFT)),
}

dir_options = {
    "|": (DOWN, UP),
    "-": (LEFT, RIGHT),
    "L": (UP, RIGHT),
    "J": (UP, LEFT),
    "7": (LEFT, DOWN),
    "F": (RIGHT, DOWN),
    "S": (DOWN, UP, LEFT, RIGHT),
}
def get_direction_vectors():
    vectors = []
    for i in range(-1,2):
        for j in range(-1,2):
            if i != j and 0 in (i,j):
                vectors.append((i,j))
    return vectors
direction_vectors = get_direction_vectors()

def invert_direction(dir):
    y, x = dir
    y *= -1
    x *= -1
    return (y,x)

def is_floor(point):
    return mapp[point[0]][point[1]] == "."

def is_start(point):
    return mapp[point[0]][point[1]] == "S"

def is_inside_map(point):
    y,x = point
    y_check = 0 <= y < len(mapp)
    x_check = 0 <= x < len(mapp[0])
    return y_check and x_check

def add_vector(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])
    
def get_possible_directions(point):
    possible = []
    y,x = point
    for direction in dir_options[mapp[y][x]]:
        step = add_vector((y,x), direction)
        if is_inside_map(step) and not is_floor(step):
            tile = mapp[step[0]][step[1]]
            for inn, _ in directions[tile]:
                if inn == direction:
                    possible.append(add_vector((y,x), direction))
    return possible
    
def print_map(mapp):
    for line in mapp:
        print(line)

def get_start_point(mapp):
    for y, value in enumerate(mapp):
        for x, value in enumerate(mapp[y]):
            if value == "S":
                return (y,x)

def calculate_step_distance(point_a, point_b):
    return abs(point_a[0]-point_b[0])+abs(point_a[1]-point_b[1])

mapp = list(map(lambda x: list(x), input_data.splitlines()))

start_point = get_start_point(mapp)
max_distance = 0

def deep_search(path):
    global max_distance
    if len(path) > 3 and is_start(path[-1]):
        for index, local in enumerate(path):
            distance = calculate_step_distance(start_point, local)
            if distance > max_distance:
                max_distance = len(path)//2
                print("New max:", max_distance )
        return
    for step in get_possible_directions(path[-1]):
        if step not in path[1:]:
            deep_search(path+[step])
import sys

# p = get_possible_directions(start_point)
# print(p)
# for point in p:
#     print(mapp[point[0]][point[1]])

sys.setrecursionlimit(100+(len(mapp)*len(mapp[0])))
deep_search([start_point])
# wrong 50
# wrong 7178, too high
# wrong 198
# 6886