# --- Day 7: Camel Cards ---

import urllib.request

def read_url(url):
    file = urllib.request.urlopen(url)
    data = file.read().strip()
    data = data.decode("utf8")
    data = data.split("\n")
    return data

def read_data(filename):
    with open(filename) as file:
        lines = list(map(str, file.readlines()))
    file.close()
    return lines

## MAIN
data = read_url("https://raw.githubusercontent.com/vxoli/advent_of_code/main/2023/d07_input.txt")
data = ['32T3K 765',
'T55J5 684',
'KK677 28',
'KTJJT 220',
'QQQJA 483',
'73456 12',
'12356 11']
# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. 
# A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. 
# The relative strength of each card follows this order, where A is the highest and 2 is the lowest.
# Every hand is exactly one type. From strongest to weakest, they are:
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
# Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.
# 
# If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. 
# If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, 
# however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, 
# continue with the third card in each hand, then the fourth, then the fifth.
# So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. 
# Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because 
# its third card is stronger (and both hands have the same first and second card).

# The first step is to put the hands in order of strength:
# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
# KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
# Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank 
# (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

# put cards into dictioary, so later can refer back and match bid values
cardDict = dict([(x.split(' ')[0], [x.split(' ')[1]]) for x in data])
# seperate out the cards played from the bid values

# sort cards based on hand type
# first count the number of same cards in the hand
# store the card label and the number of them in cardDict
for card in list(cardDict.keys()):
    cards = []
    for label in ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
        if card.count(label) > 0:
            cards += ([(label,card.count(label))])
            
    print(card , cards)
    cardDict[card].append(cards)
    match (max([x[1] for x in cards])):
        case 5:
            print("Five of a kind!")
        case 4: 
            print("Four of a kind!")
        case 3:
            print("Three of a kind!")
        case 2: #two pairs or one pair
            if [x[1] for x in cards].count(2) == 2: # two pairs
                print("Two Pairs")
            else:
                print("One pair")
        case 1: # need to check if 5 1's and cards sequential
            if (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['A', 'K', 'Q', 'J', 'T'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['K', 'Q', 'J', 'T', '9'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['Q', 'J', 'T', '9', '8'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['J', 'T', '9', '8', '7'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['T', '9', '8', '7', '6'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['9', '8', '7', '6', '5'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['8', '7', '6', '5', '4'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['7', '6', '5', '4', '3'])) or (sorted([card[0],card[1],card[2],card[3],card[4]]) == sorted(['6', '5', '4', '3', '2'])):
                print("High Hand")
            else:
                print("Bad Luck!")
                