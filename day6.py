# import math

input_data = """Time:        60     80     86     76
Distance:   601   1163   1559   1300"""

def calculate_race(max_time, hold_time):
    return (max_time - hold_time) * hold_time

time, distance = map(lambda x: x.split(":")[1].split(), input_data.splitlines())
time = list(map(lambda x: int(x), time))
distance = list(map(lambda x: int(x), distance))

races = [(time[i], distance[i]) for i in range(len(time))]

end_times = []
for time, distance in races:
    win_count = 0
    for hold_time in range(1, time+1):
        result = calculate_race(time, hold_time)
        if result > distance:
            win_count += 1
    end_times.append(win_count)

print(end_times)
# print(math.prod(end_times))

print("Part 2")
time, distance = map(lambda x: int("".join(x.split(":")[1].replace(" ",""))), input_data.splitlines())

win_count = 0
for hold_time in range(1, time+1):
    result = calculate_race(time, hold_time)
    if result > distance:
        win_count += 1

print(win_count)
