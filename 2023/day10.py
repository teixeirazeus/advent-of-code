from input_data import input_data
# input_data = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""

# input_data = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ..."""

# input_data = """..........
# .S------7.
# .|F----7|.
# .||....||.
# .||....||.
# .|L-7F-J|.
# .|..||..|.
# .L--JL--J.
# .........."""

# input_data = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ..."""

class Point():
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
    def __add__(self, point):
        y = self.y + point.y
        x = self.x + point.x
        return Point(y, x)
    
    def __str__(self):
        return f"({self.y},{self.x})"
        
    def value(self):
        return (self.y, self.x)
    
UP = Point(-1,0)
DOWN = Point(1,0)
LEFT = Point(0,-1)
RIGHT = Point(0,1)

arrow_directions = (UP, DOWN, LEFT, RIGHT)

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
        
class PipeMap():
    def __init__(self, data):
        self.map = []
        if isinstance(data, list):
            self.map = data
        else:
            for line in data.splitlines():
                self.map.append(list(line))
            
    def get_value(self, point):
        return self.map[point.y][point.x]
            
    def start_point(self):
        for y, line in enumerate(self.map):
            for x, value in enumerate(line):
                if value == "S":
                    return Point(y,x)
    
    def is_floor(self, point):
        return self.map[point.y][point.x] == "."
    
    def is_start(self, point):
        return self.map[point.y][point.x] == "S"
    
    def check_bound(self, point):
        y_check = 0 <= point.y < len(self.map)
        x_check = 0 <= point.x < len(self.map[0])
        return y_check and x_check
    
    def flood(self):
        self.map[0][0] = "~"
        used_water = True
        while used_water:
            used_water = False
            
            for y, line in enumerate(self.map):
                for x, value in enumerate(line):
                    if value == "~":
                        for d in arrow_directions:
                            step = Point(y, x)+d
                            if self.check_bound(step):
                                if self.get_value(step) == " ":
                                    self.map[step.y][step.x] = "~"
                                    used_water = True
    
    def print(self):
        for line in self.map:
            print(line)

main_map = PipeMap(input_data)
main_map.print()
print(main_map.start_point())

max_len_path = 0
max_path = None

def check_point_in_path(point, path):
    for p in path:
        if p.y == point.y and p.x == point.x:
            return True
    return False

def deep_search(path):
    global max_len_path, max_path
    if len(path) > 3 and main_map.is_start(path[-1]):
        print("Found S")
        if max_len_path < len(path):
            max_len_path = len(path) -1
            max_path = path
            return
    for dir in arrow_directions:
        if dir in dir_options[main_map.get_value(path[-1])]:
            step = path[-1]+dir
            if main_map.check_bound(step):
                if not main_map.is_floor(step):
                    step_value = main_map.get_value(step)
                    for inn, _ in directions[step_value]:
                        if inn.y == dir.y and inn.x == dir.x:
                            if not check_point_in_path(step, path[1:]):
                                deep_search(path+[step])
import sys
sys.setrecursionlimit(100+(len(main_map.map)*len(main_map.map[0])))
deep_search([main_map.start_point()])
result = max_len_path//2
print(result)
# print(main_map.start_point() in [main_map.start_point()])


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

second_map = []
for y in range(len(main_map.map)*3):
    new_line = []
    for x in range(len(main_map.map[0])*3):
        new_line.append(" ")
    second_map.append(new_line)
    
second_map = PipeMap(second_map)
        
for y, line in enumerate(main_map.map):
    for x, value in enumerate(main_map.map[y]):
        matrix = tile_to_matrix[value]
        for i in range(3):
            for j in range(3):
                y_final = (y*3)+i
                x_final = (x*3)+j
                second_map.map[y_final][x_final] = matrix[i][j]
                
second_map.flood()

def is_empty_matrix(matrix):
    empty_count = 0
    for line in matrix:
        empty_count += line.count(" ")
    return empty_count > 5


area = 0
for y, line in enumerate(main_map.map):
    for x, value in enumerate(main_map.map[y]):
        matrix = []
        for i in range(3):
            new_line = []
            for j in range(3):
                y_final = (y*3)+i
                x_final = (x*3)+j
                new_line.append(second_map.map[y_final][x_final])
            matrix.append(new_line)
        area += is_empty_matrix(matrix)

print(area)
# second_map.print()

