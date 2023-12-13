from itertools import permutations, combinations
import multiprocessing

def count_in_list(l,c):
    count = 0
    for i in l:
        if i == c:
            count += 1
    return count

def make_perm(v):
    hash_c = count_in_list(v,"#")
    dot_c = count_in_list(v,".")
    length = len(v)
    s = []
    
    def perm_rec(v, hash_c, dot_c, length):
        if len(v) == length:
            return s.append(v)
        if hash_c > 0:
            perm_rec(v+["#"], hash_c-1, dot_c, length)
        if dot_c > 0:
            perm_rec(v+["."], hash_c, dot_c-1, length)
    perm_rec([], hash_c, dot_c, length)
    return s

class HashCase:
    def __init__(self, line):
        self.debug_mode = False
        self.case, self.solution = line.split()
        self.case = self.case*5
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
        count = 0
        for vector in make_perm(self.try_vector):
            comb = self.create_combination(vector)
            if self.debug_mode:
                print("Trying", vector, comb)
            count += self.is_one_solution(comb)
        if self.debug_mode:
            print("Final solutions")
            for s in self.found_solutions:
                print("".join(self.create_combination(s)))
        return count
    
    def is_one_solution(self, result_vector):
        case = "".join(result_vector).split(".")
        has_sizes = []
        for c in case:
            if len(c) > 0:
                has_sizes.append(len(c))
        if has_sizes == self.solution:
            if result_vector not in self.found_solutions:
                if self.debug_mode:
                    print("Found", "".join(result_vector))
                    print("     ", "".join(self.case))
                    print("Sizes", has_sizes)
                    print("Solution", self.solution)
                self.found_solutions.append(result_vector)
                return True
        return False
        
    def create_combination(self, vector_comb):
        result = self.case.copy()
        i = 0
        for index, value in enumerate(self.case):
            if value == "?":
                result[index] = vector_comb[i]
                i += 1
        return result


# from input_data import input_data
input_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def get_result(x):
    return x.count_solutions()

total = 0
cases = [HashCase(line) for line in input_data.splitlines()]

with multiprocessing.Pool(processes=2) as pool:
    results = pool.map(get_result, cases)
print(sum(results))
