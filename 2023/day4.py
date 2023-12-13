# input_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
from input_data import input_data

result_part1 = 13

def calculate_matchs(player, game):
    points = game.intersection(player)
    return len(points)

def calculate_points(player, game):
    n_matchs = calculate_matchs(player, game)
    if n_matchs == 0:
        return 0
    return 2**(n_matchs-1) 
    
total = 0
for card in input_data.splitlines():
    game = card.split(":")
    player, game = card.split("|")
    player = set(player.split())
    game = set(game.split())
    total += calculate_points(player, game)

print(total)
print(total==result_part1)


# Part 2
total_of_cards = 0
card_list = []

for card in input_data.splitlines():
    game = card.split(":")
    player, game = card.split("|")
    player = set(player.split())
    game = set(game.split())
    
    card_list.append(calculate_matchs(player, game))
    
def eval_card(index):
    print("Eval card", index+1)
    global total_of_cards
    total_of_cards += 1
    for point in range(card_list[index]):
        print("- produce", index+point+1)
        eval_card(index+point+1)

print(card_list)
    
for index, card in enumerate(card_list):
    card_id = index + 1
    print("Card", card_id, "has", card_list[index], "points")
    eval_card(index)

print(total_of_cards)
print(total_of_cards == 30)
