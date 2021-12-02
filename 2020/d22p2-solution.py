with open("d22-input.txt") as f:
    lines = f.read().split("\n\n")
lines = {line.split(":")[0]: line.split(":")[1].strip() for line in lines}
lines = {key: list(map(lambda x: int(x), value.split("\n"))) for key, value in lines.items()}
card_dict = lines.copy()

p1 = card_dict["Player 1"]
p2 = card_dict["Player 2"]

i=0

# part 2 solution
# https://github.com/kermitnirmit/Advent-of-Code-2020/blob/master/day_22 solution.py
def recursive_war(p1cards, p2cards, visited):
    while(len(p1cards) > 0 and len(p2cards) > 0):
        if (tuple(p1cards), tuple(p2cards)) in visited:
            return 1, p1cards

        visited.add((tuple(p1cards), tuple(p2cards)))
        
        a, b = p1cards.pop(0), p2cards.pop(0)
        if len(p1cards) >= a and len(p2cards) >= b:
            winner, _ = recursive_war(p1cards[:a], p2cards[:b], set())
        else:
            winner = 1 if a > b else 0

        if winner == 1:
            p1cards.extend([a, b])
        else:
            p2cards.extend([b, a])
    return (1, p1cards) if len(p1cards) > 0 else (0, p2cards)
print(sum((i + 1) * x for i, x in enumerate(recursive_war(card_dict["Player 1"], card_dict["Player 2"]
, set())[1][::-1])))
	