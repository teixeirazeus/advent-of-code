from string import digits
from input_data import input_data

numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] + list(digits)

def txt_to_number(txt):
    if len(txt) == 1:
        return txt
    return str(numbers_str.index(txt) + 1)

def find_all(main_string, substring):
    indices = []
    index = main_string.find(substring)
    while index != -1:
        indices.append(index)
        index = main_string.find(substring, index + 1)
    return indices

sum_final = 0
for line in input_data.split("\n"):
    finds = []
    for number in numbers_str:
        indexes = find_all(line, number)
        for index in indexes:
            finds.append((index, number))
    sorted_finds = sorted(finds, key=lambda x: x[0])
    number = int(txt_to_number(sorted_finds[0][1]) + txt_to_number(sorted_finds[-1][1]))
    sum_final += int(txt_to_number(sorted_finds[0][1]) + txt_to_number(sorted_finds[-1][1]))
print(sum_final)


