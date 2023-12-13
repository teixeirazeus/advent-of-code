from collections import namedtuple
from input_data import input_data
# input_data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

NodeLayer = namedtuple("NodeLayer", ["source", "dest", "rangee"])

def get_map(map_name):
    mapp = []
    start_to_extract = False
    for line in input_data.splitlines():
        if start_to_extract:
            if len(line) < 2:
                return mapp
            dest, source, rangee = map(int, line.split())
            mapp.append(NodeLayer(source, dest, rangee))
        if map_name in line:
            start_to_extract = True
    return mapp

def get_seeds():
    return list(map(int, input_data.splitlines()[0].split(":")[1].split()))

maps_order = ("seed-to-soil",
              "soil-to-fertilizer",
              "fertilizer-to-water",
              "water-to-light",
              "light-to-temperature",
              "temperature-to-humidity",
              "humidity-to-location")

mapp_cache = {}
def get_map_by_index(map_index):
    if map_index not in mapp_cache.keys():
        mapp_cache[map_index] = get_map(maps_order[map_index])
    return mapp_cache[map_index] 

def check_if_is_in_range(node_value, node_layer):
    return node_layer.source <= node_value < node_layer.source+node_layer.rangee


def next_node(node, mapp):
    for node_layer in mapp:
        if check_if_is_in_range(node, node_layer):
            diff = node - node_layer.source
            return node_layer.dest + diff
    return node

def deep_search(node):
    for map in maps:
        node = next_node(node, map)
    return node
        
        
# print("Part 2")
seeds = get_seeds()

lower_location = None
maps = []
for map_name in maps_order:
    maps.append(get_map(map_name))

for i in range(0, len(seeds), 2):
    for seed in range(seeds[i], seeds[i]+seeds[i+1]):
        location = deep_search(seed)
        if lower_location is None or lower_location > location:
            lower_location = location
        
print(lower_location)
print(lower_location == 46)