from input_data import input_data
# input_data = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""


case = list(map(list, input_data.splitlines()))


def print_case(case):
    for line in case:
        print("".join(line))


def tilt_north(case):
    tilt = True
    while tilt:
        tilt = False
        for y, line in enumerate(case):
            for x, value in enumerate(line):
                if y != 0:
                    if value == "O" and case[y - 1][x] == ".":
                        tilt = True
                        case[y - 1][x] = "O"
                        case[y][x] = "."
    return case


def tilt_south(case):
    tilt = True
    while tilt:
        tilt = False
        for y, line in enumerate(case):
            for x, value in enumerate(line):
                if y != len(case) - 1:
                    if value == "O" and case[y + 1][x] == ".":
                        tilt = True
                        case[y + 1][x] = "O"
                        case[y][x] = "."
    return case


def tilt_right(case):
    tilt = True
    while tilt:
        tilt = False
        for y, line in enumerate(case):
            for x, value in enumerate(line):
                if x != len(case) - 1:
                    if value == "O" and case[y][x + 1] == ".":
                        tilt = True
                        case[y][x + 1] = "O"
                        case[y][x] = "."
    return case


def tilt_left(case):
    tilt = True
    while tilt:
        tilt = False
        for y, line in enumerate(case):
            for x, value in enumerate(line):
                if x != 0:
                    if value == "O" and case[y][x - 1] == ".":
                        tilt = True
                        case[y][x - 1] = "O"
                        case[y][x] = "."
    return case


def cycle(case):
    return tilt_right(tilt_south(tilt_left(tilt_north(case))))


def calculate_load(case):
    total = 0
    for y, line in enumerate(case):
        for x, value in enumerate(line):
            if value == "O":
                total += len(case) - y
    return total


print_case(case)
print("____")
for i in range(1000):
    case = cycle(case)
    if i == 999:
        print(">", calculate_load(case))
    # if calculate_load(case) == 64:
    #     print(i)
    # input()
print(calculate_load(case))
print(5)
