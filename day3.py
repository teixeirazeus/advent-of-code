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
result = 4361

result_part2 = 467835

engine_matrix = []
def load_matrix():
    engine_matrix = []
    for line in input_data.split("\n"):
        engine_line = []
        for w in line:
            engine_line.append(w)
        engine_matrix.append(engine_line)
    return engine_matrix
engine_matrix = load_matrix()
    
def explode_number(x_origin, y_origin):
    # print("Explode", x_origin, y_origin, engine_matrix[y_origin][x_origin])
    engine_matrix[y_origin][x_origin] = "."
    x = x_origin
    while True:
        x -= 1
        if x < 0:
            break
        if engine_matrix[y_origin][x].isdigit():
            engine_matrix[y_origin][x] = "."
        else:
            break
    x = x_origin
    while True:
        x += 1
        if x >= len(engine_matrix[y_origin]):
            break
        # print("Consulta", engine_matrix[y_origin][x])
        if engine_matrix[y_origin][x].isdigit():
            engine_matrix[y_origin][x] = "."
        else:
            break
    
def has_simbol_adjents(x, y):
    adjents = grab_adjents(x, y)
    for simbol in adjents:
        if not simbol.isdigit() and simbol != ".":
            return True
    return False
    
def grab_adjents(x, y):
    # print("Grab", x, y, engine_matrix[y][x], end=": ")
    diretions = ((-1,1), (0,1), (1,1), 
                 (-1,0), (1,0), 
                 (-1,-1), (0,-1), (1,-1))
    adjents = []
    for x_add, y_add in diretions:
        if (x_add+x) >= 0 and (y_add+y) >= 0 and x_add+x < len(engine_matrix[y]) and y_add+y < len(engine_matrix):
            adjents.append(engine_matrix[y+y_add][x+x_add])
    return adjents

for y in range(len(engine_matrix)):
    for x in range(len(engine_matrix[y])):
        if has_simbol_adjents(x,y) and engine_matrix[y][x].isdigit():
            explode_number(x,y)

sum_total = 0
for line in engine_matrix:
    line = "".join(line).split(".")
    for l in line:
        if l.isdigit():
            print(l, "is digit")
            sum_total -= int(l)
print(sum_total)

engine_matrix = load_matrix()
for y in range(len(engine_matrix)):
    for x in range(len(engine_matrix[y])):
        if not engine_matrix[y][x].isdigit():
            engine_matrix[y][x] = "."

for line in engine_matrix:
    line = "".join(line).split(".")
    print(">", line)
    for l in line:
        if l.isdigit():
            sum_total += int(l)
            
print(sum_total)
print(result == sum_total)


def get_full_number(x_origin, y_origin, new_matrix):
    x = x_origin
    while True:
        x -= 1
        if x < 0:
            break
        if engine_matrix[y_origin][x].isdigit():
            new_matrix[y_origin][x] = engine_matrix[y_origin][x]
        else:
            break
    x = x_origin
    while True:
        x += 1
        if x >= len(engine_matrix[y_origin]):
            break
        # print("Consulta", engine_matrix[y_origin][x])
        if engine_matrix[y_origin][x].isdigit():
            new_matrix[y_origin][x] = engine_matrix[y_origin][x]
        else:
            break
    return new_matrix

def grab_adjents_full_number(x, y):
    new_matrix = make_new_matrix()
    diretions = ((-1,1), (0,1), (1,1), 
                 (-1,0), (1,0), 
                 (-1,-1), (0,-1), (1,-1))
    numbers = []
    for x_add, y_add in diretions:
        if (x_add+x) >= 0 and (y_add+y) >= 0 and x_add+x < len(engine_matrix[y]) and y_add+y < len(engine_matrix):
            y_now = y+y_add
            x_now = x+x_add
            if engine_matrix[y_now][x_now].isdigit():
                new_matrix[y_now][x_now] = engine_matrix[y_now][x_now]
                new_matrix = get_full_number(x_now, y_now, new_matrix)
    for line in new_matrix:
        line = "".join(line).split(".")
        for l in line:
            if l.isdigit():
                numbers.append(l)
    return numbers


# parte 2
engine_matrix = load_matrix()

def make_new_matrix():
    new_matrix = []
    for line in engine_matrix:
        new_matrix.append(["." for l in line])
    return new_matrix

total = 0
for y in range(len(engine_matrix)):
    for x in range(len(engine_matrix[y])):
        if engine_matrix[y][x] == "*":
            numbers = grab_adjents_full_number(x, y)
            if len(numbers) == 2:
                total += int(numbers[0]) * int(numbers[1])

print(total)
print(total == result_part2)