import itertools
from input_data import input_data
# input_data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""


def has_galaxy(line):
    for x in line:
        if x == "#":
            return True
    return False

def has_galaxy_vertical(space, x_index):
    for y in range(len(space)):
        if space[y][x_index] == "#":
            return True
    return False

def load_space_map(data):
    space = []
    for line in data.splitlines():
        if not has_galaxy(line):
            space.append(["X"]*len(line))
        else:
            space.append(list(line))
    
    new_space = [[] for y in range(len(space))]
    
    for x_look in range(len(space[0])):
        if not has_galaxy_vertical(space, x_look):
            for y in range(len(space)):
                new_space[y].append("X")
        else:
            for y in range(len(space)):
                new_space[y].append(space[y][x_look])
                
    return new_space

def get_galaxys(space):
    galaxys = []
    for y, line in enumerate(space):
        for x, value in enumerate(line):
            if value == "#":
                galaxys.append((y,x))
    return galaxys

# space_expansion = 2
space_expansion = 1000000
space = load_space_map(input_data)
galaxys = get_galaxys(space)

for line in space:
    print(line)
print("-")
print(galaxys)

def manhatan_discante(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def get_local_distance(point):
    global space_expansion
    if space[point[0]][point[1]] != "X":
        return 1
    return space_expansion

def calculate_distance(start, end):
    end = list(end)
    now = list(start)
    distance = 0
    # try move y
    while now != end:
        if now[0] != end[0]:
            if now[0] > end[0]:
                now[0] -= 1
            else:
                now[0] += 1
        elif now[1] != end[1]:
            if now[1] > end[1]:
                now[1] -= 1
            else:
                now[1] += 1
            
        distance += get_local_distance(now)
    return distance
            
                
def galaxy_search_path_size():
    path_size = 0
    for a,b in itertools.combinations(galaxys, 2):
        path_size += calculate_distance(a,b)
    return path_size

print(galaxy_search_path_size())

print(calculate_distance((9,0),(9,4)))
# print(calculate_distance((9,0),(9,4)) == 5)

print(galaxy_search_path_size() ==  9556896)
