input_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def count(case, solution):
    case_l = list(case)
    question_indexs = []
    for index, value in enumerate(case_l):
        if value == "?":
            question_indexs.append(index)
    hash_total = sum(solution)
    dot_total = len(question_indexs)

    def f(case_l, hash, dot, questions):
        result = 0
        if len(questions) == 0:
            case = "".join(case_l).split(".")
            return solution == tuple([len(c) for c in case if len(c) > 0])
        if hash > 0:
            case_l[questions[0]] = "#"
            result += f(case_l, hash - 1, dot, questions[1:])
        if dot > 0:
            case_l[questions[0]] = "."
            result += f(case_l, hash, dot - 1, questions[1:])
        return result

    return f(case_l, hash_total, dot_total, question_indexs)


from functools import cache


def count_v2(case, solution):
    case_l = "." + case + "."

    @cache
    def f(index, s_index, block_size):
        # se chegou no final
        if index == len(case_l):
            if s_index == len(solution) and block_size == 0:
                # e preencheu todos os slots
                return 1
            return 0

        # se estorou o index de slot
        if s_index > len(solution):
            return 0

        result = 0
        if case_l[index] == ".":
            if block_size == 0:
                if s_index < len(solution):
                    result += f(index + 1, s_index + 1, solution[s_index])
                result += f(index + 1, s_index, 0)
        elif case_l[index] == "#":
            if block_size > 0:
                result += f(index + 1, s_index, block_size - 1)
        else:
            # ?
            if block_size == 0:
                if s_index < len(solution):
                    result += f(index + 1, s_index + 1, solution[s_index])
                result += f(index + 1, s_index, 0)

            if block_size > 0:
                result += f(index + 1, s_index, block_size - 1)
        return result

    return f(0, 0, 0)


result = 0
for line in input_data.splitlines():
    case, nums = line.split()

    case = "?".join([case] * 5)
    nums += ","
    nums *= 5
    nums = nums[:-1]

    nums = tuple(map(int, nums.split(",")))
    c = count_v2(case, nums)
    print(line, result)
    result += c
print(result)
print(result == 21)
