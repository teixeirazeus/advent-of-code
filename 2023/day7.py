

def get_hand_power_value(hand):
    cards = set(list(hand))
    counts = []
    for card in cards:
        counts.append(hand.count(card))
    counts.sort(reverse=True)
    
    high_card = [1,1,1,1,1]
    if counts == high_card:
        return 1
    one_pair = [2,1,1,1]
    if counts == one_pair:
        return 2
    two_pair = [2,2,1]
    if counts == two_pair:
        return 3
    tree_of_kind = [3,1,1]
    if counts == tree_of_kind:
        return 4
    full_house = [3,2]
    if counts == full_house:
        return 5
    four_of_kind = [4,1]
    if counts == four_of_kind:
        return 6
    five_of_kind = [5]
    if counts == five_of_kind:
        return 7
    raise Exception("Card power not found")

card_rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
print(len(card_rank))


def get_card_index(card):
    index = card_rank.index(card)
    if index == -1:
        raise Exception("Card not found")
    return index
    

# input_data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
from input_data import input_data


def compare_hands(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    value1 = get_hand_power_value(hand1)
    value2 = get_hand_power_value(hand2)
    if value1 > value2:
        return -1
    elif value1 < value2:
        return 1
    else:
        for i, card_a in enumerate(hand1):
            card_b = hand2[i]
            if card_a == card_b:
                continue
            if get_card_index(card_a) > get_card_index(card_b):
                return 1
            else:
                return -1
    return 0

from functools import cmp_to_key
compare_hands_key = cmp_to_key(compare_hands)

print(compare_hands(["AAAAA", 0], ["AAAAT", 0]))

game = []
for line in input_data.splitlines():
    hand, bid = line.split()
    game.append([hand, bid])

game.sort(key=compare_hands_key)
game = game[::-1]
total = 0
for i, play in enumerate(game):
    total += (i+1)*int(play[1])
    
print(total)
# 248978897 - wrong
# 249971027 - wrong


print("PART 2")

# input_data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

card_rank = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def get_hand_power_value(hand):
    def get_power(hand):
        cards = set(list(hand))
        counts = []
        for card in cards:
            counts.append(hand.count(card))
        counts.sort(reverse=True)
        
        high_card = [1,1,1,1,1]
        if counts == high_card:
            return 1
        one_pair = [2,1,1,1]
        if counts == one_pair:
            return 2
        two_pair = [2,2,1]
        if counts == two_pair:
            return 3
        tree_of_kind = [3,1,1]
        if counts == tree_of_kind:
            return 4
        full_house = [3,2]
        if counts == full_house:
            return 5
        four_of_kind = [4,1]
        if counts == four_of_kind:
            return 6
        five_of_kind = [5]
        if counts == five_of_kind:
            return 7
        raise Exception("Card power not found")
    if "J" not in hand:
        return get_power(hand)
    else:
        max_value = 0
        for possible_card in card_rank:
            value = get_power(hand.replace("J", possible_card))
            if value > max_value:
                max_value = value
        return max_value


game = []
for line in input_data.splitlines():
    hand, bid = line.split()
    game.append([hand, bid])

game.sort(key=compare_hands_key)
game = game[::-1]
total = 0
for i, play in enumerate(game):
    total += (i+1)*int(play[1])

print(total)
# 250680561 - wrong

