from input_data import input_data

# input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def part_one():
    def check_limitations(game) -> int:
        def subset_pass_the_limit(subset) -> bool:
            limit = {"red": 12, "green": 13, "blue": 14}
            for cube in subset.split(","):
                count, color  = cube.split()
                if int(count) > limit[color]:
                    return True
            return False
        
        game_info, game_data = game.split(":")
        game_id = int(game_info.split()[1])
        for subgame in game_data.split(";"):
            if subset_pass_the_limit(subgame):
                return 0
        return game_id

    sum_total = 0
    for game in input_data.split("\n"):
        sum_total += check_limitations(game)
    print(sum_total)

def part_two():
    sum_total = 0
    for game in input_data.split("\n"):
        _, game_data = game.split(":")
        count = {"red": 0, "green": 0, "blue": 0}
        for subgame in game_data.split(";"):
            for cube in subgame.split(","):
                value, color  = cube.split()
                if count[color] < int(value):
                    count[color] = int(value)
        sum_total += count["red"] * count["green"] * count["blue"]

    print(sum_total)
part_two()