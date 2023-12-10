# input_data = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""
from input_data import input_data

def get_instructions():
    return input_data.splitlines()[0]

def load_nodes():
    nodes = {}
    for node_line in input_data.splitlines()[2:]:
        node_key, directions = node_line.split("=")
        left, right = directions.replace("(","").replace(")","").split(",")
        nodes[node_key.strip()] = {"left": left.strip(), "right": right.strip()}
    return nodes

instructions = get_instructions()
nodes = load_nodes()

step = 0
actual_node = "AAA"
found_end = False
while not found_end:
    for direction in instructions:
        if actual_node == "ZZZ":
            found_end = True
            break
        if direction == "R":
            actual_node = nodes[actual_node]["right"]
        else:
            actual_node = nodes[actual_node]["left"]
        step += 1

print(step)
print(step == 2)

print("Part 2")
# input_data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""


def get_start_nodes(nodes):
    start_nodes = []
    for node in nodes.keys():
        if node[-1] == "A":
            start_nodes.append(node)
    return start_nodes

def get_end_nodes(nodes):
    end_nodes = []
    for node in nodes.keys():
        if node[-1] == "Z":
            end_nodes.append(node)
    return end_nodes

def all_is_none(node_key_list):
    for n in node_key_list:
        if n != None:
            return False
    return True

instructions = get_instructions()
nodes = load_nodes()
actual_node_list = get_start_nodes(nodes)

def end_of_route(nodes_list):
    for node in nodes_list:
        if node[-1] != "Z":
            return False
    return True

import math
times = {}
def get_steps(node_list):
    step = 0
    while True:
        for direction in instructions:
            if end_of_route(node_list):
                return step
            for index, node in enumerate(node_list):
                if node[-1] == "Z":
                    times[index] = step
                if len(times) == len(actual_node_list):
                    print(">", math.lcm(*list(times.values())))
                    return step
            if direction == "R":
                for index, node in enumerate(node_list):
                    node_list[index] = nodes[node]["right"]
            else:
                for index, node in enumerate(node_list):
                    node_list[index] = nodes[node]["left"]
            step += 1
            
step = get_steps(actual_node_list)
print(step)
print(step == 6)