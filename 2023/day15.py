def get_hash(text):
    value = 0
    for char in text:
        value += ord(char)
        value *= 17
        value = value % 256
    return value


# part 1
# long_text = input()
# result = 0
# for code in long_text.split(","):
#     result += get_hash(code)
# print(result)

# part 2
long_text = input()
# long_text = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
result = 0
hash_map = {}
for code in long_text.split(","):
    if "=" in code:
        label, value = code.split("=")
        value = int(value)
        key = get_hash(label)

        if key not in hash_map.keys():
            hash_map[key] = [(label, value)]
        else:
            new_list = []
            found_key = False
            for label_local, value_local in hash_map[key]:
                if label == label_local:
                    found_key = True
                    new_list.append((label, value))
                else:
                    new_list.append((label_local, value_local))
            if not found_key:
                new_list.append((label, value))
            hash_map[key] = new_list
    else:
        label = code.replace("-", "")
        key = get_hash(label)
        if key in hash_map.keys():
            hash_map[key] = [
                (label_arg, value_arg)
                for label_arg, value_arg in hash_map[key]
                if label_arg != label
            ]
    print(code, hash_map)

print(hash_map)

print("Calculation")
result = 0
for key in hash_map:
    for index, lens in enumerate(hash_map[key]):
        label, value = lens
        result += (key + 1) * (index + 1) * value
print(result)


# wrong 10351, too low
