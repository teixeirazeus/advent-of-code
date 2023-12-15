import functools

from input_data import input_data
# input_data = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

# input_data = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""


def load_cases(data):
    cases = []
    case = []
    for line in data.splitlines():
        # print(line, len(line))
        if len(line) == 0:
            cases.append(case)
            case = []
            continue
        case.append(list(line))
    cases.append(case)
    return cases


def print_case(case):
    for line in case:
        print("".join(line))


def rotate_matrix(matrix):
    return list(zip(*matrix[::-1]))


def compare_cut(a, b):
    for i in range(min(len(a), len(b))):
        if a[-i - 1] != b[i]:
            return False
    return True


def mirror_line(line):
    indexes = set()
    for x_lock in range(1, len(line)):
        if compare_cut(line[:x_lock], line[x_lock:]):
            indexes.add(x_lock)
    # print("".join(line), indexes)
    return indexes


def try_match(case):
    matchs_all = []
    for line in case:
        matchs = mirror_line(line)
        matchs_all.append(matchs)
    return list(functools.reduce(lambda a, b: a.intersection(b), matchs_all))


cases = load_cases(input_data)


def get_result(case):
    m = try_match(case)
    if len(m) > 0:
        return m[0]
    else:
        m = try_match(rotate_matrix(case))
        if len(m) > 0:
            return (len(case) - m[0]) * 100
    return 0


def flip(value):
    if value == "#":
        return "."
    return "#"


def get_result_p2(case):
    first_solution = get_result(case)
    for y, line in enumerate(case):
        for x, value in enumerate(line):
            try_case = [[i for i in l] for l in case]
            try_case[y][x] = flip(value)
            r = try_match(try_case)
            for i in r:
                if i not in (0, first_solution):
                    return i
            c = try_match(rotate_matrix(try_case))
            for i in c:
                result = (len(case) - i) * 100
                if result not in (0, first_solution):
                    return result
    print("*")
    print_case(case)
    print("*")
    return 0


# print("Result", get_result_p2(cases[1]))
# print(max_size_slot)


result = []
for i, case in enumerate(cases):
    result.append(get_result_p2(case))
# for i in result:
#     print(i)
print(sum(result))


# wrong 22451
# wrong 32814, for every math, add
# wrong 36849
# right 34202


# p2
# wrong 35031 too high
# wrong 33900
# wrong 25900 too low
# right 34230
