import multiprocessing

def count_in_list(l,c):
    count = 0
    for i in l:
        if i == c:
            count += 1
    return count

class HashCase:
    def __init__(self, line):
        self.debug_mode = False
        self.part_two_mode = True
        self.case, self.solution = line.split()
        
        # part 2
        if self.part_two_mode:
            self.case = "?".join([self.case]*5)
            self.solution += ","
            self.solution *= 5
            self.solution = self.solution[:-1]
        
        self.case = list(self.case)
        self.solution = list(map(int, self.solution.split(",")))
        self.hash_count_case = 0
        for i in self.case:
            if i == "#":
                self.hash_count_case += 1
        self.hash_count_solution = sum(self.solution)
        self.slots = 0
        for i in self.case:
            if i == "?":
                self.slots += 1
        self.remaning_hash = self.hash_count_solution-self.hash_count_case
        self.try_vector = ["#"]*self.remaning_hash
        while len(self.try_vector) != self.slots:
            self.try_vector.append(".")
        self.found_solutions = []
        if self.debug_mode:
            print("HashCase")
            print("Slots", self.slots)
            print("Hashs", self.hash_count_case)
            print("Hashs Solutions", self.hash_count_solution)
            print("Try vector", self.try_vector)
    
    def count_solutions(self):
        self.count = 0
        
        hash_c = count_in_list(self.try_vector,"#")
        dot_c = count_in_list(self.try_vector,".")
        length = len(self.try_vector)
        
        def perm_rec(v, hash_c, dot_c, length):
            if len(v) == length:
                comb = self.create_combination(v)
                self.count += self.is_one_solution(comb)
            if hash_c > 0:
                perm_rec(v+["#"], hash_c-1, dot_c, length)
            if dot_c > 0:
                perm_rec(v+["."], hash_c, dot_c-1, length)
        perm_rec([], hash_c, dot_c, length)
            
        return self.count
    
    def is_one_solution(self, result_vector):
        case = "".join(result_vector).split(".")
        has_sizes = [len(c) for c in case if len(c) > 0]
        if len(has_sizes) != len(self.solution):
            return False
        for i in range(len(has_sizes)):
            if has_sizes[i] != self.solution[i]:
                return False
        return True
    
    def create_combination(self, vector_comb):
        result = self.case.copy()
        i = 0
        for index, value in enumerate(self.case):
            if value == "?":
                result[index] = vector_comb[i]
                i += 1
        return result


from input_data import input_data
# input_data = """???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1"""



# # print(HashCase("???.### 1,1,3").count_solutions())
# cases = [HashCase(line) for line in input_data.splitlines()]


# version 2
from functools import cache

@cache
def count(case, slots):
    if case == "":
        return 1 if slots == () else 0
    
    if slots == ():
        return 0 if "#" in case else 1
    
    result = 0
    
    if case[0] in ".?":
        result += count(case[1:], slots)
    
    if case[0] in "#?":
        if slots[0] <= len(case) and "." not in case[:slots[0]] and (slots[0] == len(case) or case[slots[0]] != "#"):
            result += count(case[slots[0]+1:], slots[1:])
    
    return result
    
cases = []
for line in input_data.splitlines():
    cfg, nums = line.split()

    cfg = "?".join([cfg]*5)
    nums += ","
    nums *= 5
    nums = nums[:-1]
    
    nums = tuple(map(int, nums.split(",")))
    cases.append((cfg, nums))

def get_result(case):
    return count(case[0], case[1])

with multiprocessing.Pool(processes=20) as pool:
    results = pool.map(get_result, cases)
print(sum(results))


# version 3
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
            result += f(case_l, hash-1, dot, questions[1:])
        if dot > 0:
            case_l[questions[0]] = "."
            result += f(case_l, hash, dot-1, questions[1:])
        return result
    
    return f(case_l, hash_total, dot_total, question_indexs)
    
    
cases = []
for line in input_data.splitlines():
    cfg, nums = line.split()

    cfg = "?".join([cfg]*5)
    nums += ","
    nums *= 5
    nums = nums[:-1]
    
    nums = tuple(map(int, nums.split(",")))
    cases.append((cfg, nums))

def get_result(case):
    return count(case[0], case[1])

with Pool(processes=20) as pool:
    results = pool.map(get_result, cases)
print(sum(results))
