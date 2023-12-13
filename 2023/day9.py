# input_data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""
from input_data import input_data

cases = []
for case in input_data.splitlines():
    cases.append(map(int, case.split()))

def all_zeros(s):
    for i in s:
        if i != 0:
            return False
    return True

def gen_next_seq(seq):
    new_seq = []
    for index, number in enumerate(seq[:-1]):
        next_number = seq[index+1]
        diff = next_number-number
        new_seq.append(diff)
    return new_seq

def get_last_numbers(seq):
    last_numbers = [seq[-1]]
    while not all_zeros(seq):
        seq = gen_next_seq(seq)
        last_numbers.append(seq[-1])
    return last_numbers

result = 0
for case in cases:
    result += sum(get_last_numbers(case))
print(result)
print(result == 114)

print("Part 2")
def get_first_numbers(seq):
    print("GET Seq", seq)
    first_numbers = [seq[0]]
    while not all_zeros(seq):
        seq = gen_next_seq(seq)
        print("-", seq)
        first_numbers.append(seq[0])
    print("First numbers", first_numbers)
    return first_numbers

# first = get_first_numbers(map(int, "-4, -1, 5, 14, 26, 41, 59, 80, 104, 131, 161, 194".split(",")))
# print(first)
# print(sum(first))
# print(-sum(first)-4)
result = 0
for case in cases:
    first_numbers = get_first_numbers(case)
    for index, number in enumerate(first_numbers):
        if index % 2 == 0:
            result += number
        else:
            result -= number
# -3 0 5
print(result)
print(result == 2)
    
# wrong 3052 too high
# wrong -17290
# wrong -21478
# wrong -15196
# wrong 17290


