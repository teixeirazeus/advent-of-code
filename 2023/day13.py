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
        print(line, len(line))
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
    results = set()
    first = get_result(case)
    results.add(first)
    results.add(0)
    for y, line in enumerate(case):
        for x, value in enumerate(line):
            try_case = [[i for i in l] for l in case]
            try_case[y][x] = flip(value)
            # print(y, x)
            # print_case(try_case)
            # input()
            r = try_match(case)
            if len(r) > 0:
                results.add(r[0])
            c = try_match(rotate_matrix(try_case))
            if len(c) > 0:
                results.add((len(case) - c[0]) * 100)
            print(results)
    results.remove(first)
    results.remove(0)
    results = list(results)
    if len(results) > 0:
        return results[0]
    else:
        print("Case not found")
        print_case(case)
        return 0


# print("Result", get_result_p2(cases[1]))
# print(max_size_slot)


result = []
for i, case in enumerate(cases):
    result.append(get_result_p2(case))
for i in result:
    print(i)
print(sum(result))


# wrong 22451
# wrong 32814, for every math, add
# wrong 36849
# right 34202


# p2
# wrong 35031 too high
# wrong 25900 too low
