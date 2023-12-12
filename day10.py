from input_data import input_data
# input_data = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""

# input_data = """...........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# .........."""

# input_data = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L"""

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

def is_inside_map_arg(point, local_map):
    y,x = point
    y_check = 0 <= y < len(local_map)
    x_check = 0 <= x < len(local_map[0])
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
max_path = []

def deep_search(path):
    global max_distance, max_path
    if len(path) > 3 and is_start(path[-1]):
        for index, local in enumerate(path):
            distance = calculate_step_distance(start_point, local)
            if distance > max_distance:
                max_distance = len(path)//2
                max_path = path
                print("New max:", max_distance)
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


# p1
# wrong 50
# wrong 7178, too high
# wrong 198
# 6886

import os
import time

print("Part 2")

tile_to_matrix = {
    "|": [[" ", "X", " "],
          [" ", "X", " "],
          [" ", "X", " "]],
    "-": [[" ", " ", " "],
          ["X", "X", "X"],
          [" ", " ", " "]],
    "L": [[" ", "X", " "],
          [" ", "X", "X"],
          [" ", " ", " "]],
    "J": [[" ", "X", " "],
          ["X", "X", " "],
          [" ", " ", " "]],
    "7": [[" ", " ", " "],
          ["X", "X", " "],
          [" ", "X", " "]],
    "F": [[" ", " ", " "],
          [" ", "X", "X"],
          [" ", "X", " "]],
    "S": [[" ", "X", " "],
          ["X", "X", "X"],
          [" ", "X", " "]],
    ".": [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]],
}

# for p in max_path:
#     print(p)
#     mapp[p[0]][p[1]] = "X"
#     os.system('clear')
#     print_map(mapp)
#     time.sleep(1)
    
drawn_mapp = []

for y in range(len(mapp)*3):
    new_line = []
    for x in range(len(mapp[0])*3):
        new_line.append(" ")
    drawn_mapp.append(new_line)

for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        tile = mapp[y][x]
        tile_matrix = tile_to_matrix[tile]
        for y_m in range(len(tile_matrix)):
            for x_m in range(len(tile_matrix[y_m])):
                drawn_mapp[(y*3)+y_m][(x*3)+x_m] = tile_matrix[y_m][x_m]

def flood_map(local_map):
    local_map[0][0] = "~"
    
    used_water = True
    while used_water:
        used_water = False
        for y, line in enumerate(local_map):
            for x, value in enumerate(line):
                if value == "~":
                    for direction in (UP, DOWN, LEFT, RIGHT):
                        step = add_vector((y,x), direction)
                        if is_inside_map_arg(step, local_map):
                            if local_map[step[0]][step[1]] not in ["X", "~"]:
                                local_map[step[0]][step[1]] = "~"
                                used_water = True
    return local_map

# def empty_count(real_map, local_map):
#     for y, line in enumerate(real_map):
#         for x, value in enumerate(real_map):
#             for


def get_result_matrix(y_start, x_start):
    result_matrix = []
    y = y_start*3
    x = x_start*3
    for y_m in range(y, y+3):
        new_line = []
        for x_m in range(x, x+3):
            new_line.append(drawn_mapp[y_m][x_m])
        result_matrix.append(new_line)
    return result_matrix
    
def is_empty(matrix):
    empty_count = 0
    for line in matrix:
        for value in line:
            if value == " ":
                empty_count += 1
    return empty_count > 5
        
print_map(drawn_mapp)
drawn_mapp = flood_map(drawn_mapp)
print_map(drawn_mapp)
count = 0

for y in range(len(mapp)):
    for x in range(len(mapp[y])):
        result_matrix = get_result_matrix(y, x)
        print_map(result_matrix)
        print("-")
        if is_empty(result_matrix):
            count += 1
print(count)
# area = 0
# for y, line in enumerate(drawn_mapp):
#     found_x = False
#     x_local = -1
#     for x, tile in enumerate(line):
#         if tile == "X" and not found_x:
#             found_x = True
#             x_local = x
#             continue
#         elif tile == "X" and found_x:
#             if x_local == -1:
#                 raise Exception("x_local is negative")
#             found_x = False
#             area += x-x_local-1
# print(area)
# print_map(drawn_mapp)


# p2
# 647 wrong, too high