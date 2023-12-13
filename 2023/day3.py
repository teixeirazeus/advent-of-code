# input_data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
from input_data import input_data

result_part1 = 549908
result_part2 = 81166799

def print_engine(matrix):
    for line in matrix:
        print(line)

def load_engine():
    matrix = []
    for line in input_data.splitlines():
        matrix.append(list(line))
    return matrix

def load_blank_engine():
    matrix = []
    for line in input_data.splitlines():
        matrix.append(list(line))
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            matrix[y][x] = "."
    return matrix

def is_symbol(value):
    return not value.isdigit() and value != "."

def get_full_number(x,y, blank_engine):
    blank_engine[y][x] = engine[y][x]
    
    new_x = x
    while True:
        new_x -= 1
        if new_x < 0:
            break
        if engine[y][new_x].isdigit():
            blank_engine[y][new_x] = engine[y][new_x]
        else:
            break
    
    new_x = x
    while True:
        new_x += 1
        if new_x >= len(engine[y]):
            break
        if engine[y][new_x].isdigit():
            blank_engine[y][new_x] = engine[y][new_x]
        else:
            break
    
    return blank_engine
    
            
def scan_adj(x, y, blank_engine):
    directions = ((-1,-1), (0, -1), (1,-1),
                  (-1,0), (1,0),
                  (-1,1), (0,1), (1,1))
    for y_add, x_add in directions:
        new_x = x + x_add
        new_y = y + y_add
        if new_x >= 0 and new_y >= 0 and new_x < len(engine[y]) and new_y < len(engine):
            value = engine[new_y][new_x]
            if value.isdigit():
                blank_engine = get_full_number(new_x, new_y, blank_engine)
    return blank_engine
            

engine = load_engine()
blank_engine = load_blank_engine()

for y in range(len(engine)):
    for x in range(len(engine[y])):
        if is_symbol(engine[y][x]):
            blank_engine = scan_adj(x, y, blank_engine)
            
total = 0
for line in blank_engine:
    for c in "".join(line).split("."):
        if c.isdigit():
            total += int(c)
            
print_engine(blank_engine)

print(total)
print(total == result_part1)

print("PART 2")
engine = load_engine()


def get_numbers(blank_engine):
    numbers = []
    for line in blank_engine:
        for c in "".join(line).split("."):
            if c.isdigit():
                numbers.append(c)
    return numbers

total = 0

for y in range(len(engine)):
    for x in range(len(engine[y])):
        if engine[y][x] == "*":
            blank_engine = load_blank_engine()
            blank_engine = scan_adj(x, y, blank_engine)
            numbers = get_numbers(blank_engine)
            print("Find start!", numbers)
            if len(numbers) == 2:
                total += int(numbers[0]) * int(numbers[1])

print(total)
print(total == result_part2)