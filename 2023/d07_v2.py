from collections import Counter


def get_hands(filename):
    hands = []
    with open(filename) as f:
        for line in f:
            hand, bid = line.strip().split()
            hands.append((list(hand), int(bid)))
    
    return hands


def score_hand_type(hand):
    freqs = list(Counter(hand).values())
    match (len(freqs), max(freqs)):
        case (5, _): return 0
        case (4, _): return 1
        case (3, 2): return 2
        case (3, _): return 3
        case (2, 3): return 4
        case (2, _): return 5
        case (1, _): return 6
        
    
def score_cards(hand, cards_strength):    
    # hand is encoded in base 13, convert it to base 10
    result = 0
    base = 13
    for i, card in enumerate(reversed(hand)):
        result += cards_strength[card] * (base ** i)
    
    return result


def utility(hand, cards_strength):
    return score_hand_type(hand) * 1_000_000 + score_cards(hand, cards_strength)


hands = get_hands("d07_input.txt")
cards_strength = {c: i for i, c in enumerate('23456789TJQKA')}
utilities = [utility(hand, cards_strength) for hand, _ in hands]
ranks = [sorted(utilities).index(x) + 1 for x in utilities]
print(ranks)
winnings = sum(rank * bid for rank, (_, bid) in zip(ranks, hands))

print(winnings)
