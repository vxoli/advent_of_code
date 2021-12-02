with open("d22-input.txt") as f:
    lines = f.read().split("\n\n")
lines = {line.split(":")[0]: line.split(":")[1].strip() for line in lines}
lines = {key: list(map(lambda x: int(x), value.split("\n"))) for key, value in lines.items()}
card_dict = lines.copy()

p1 = card_dict["Player 1"]
p2 = card_dict["Player 2"]

i=0
while len(p1) != 0 or len(p2) != 0:
	# play the top card
	card1 = p1[0]
	card2 = p2[0]
	# remove top card from the hand
	del(p1[0])
	del(p2[0])
	# player1 card wins append player 1 card to bottom of hand followed by player 2 card
	if card1 > card2:
		p1.append(card1)
		p1.append(card2)
	else:
	# player 2 card wins append player 2 card bottom of hand followed by player 1 card
		p2.append(card2)
		p2.append(card1)
	i += 1
	if len(p1) == 0 or len (p2) == 0:
		break
if len(p1) == 0: # player 2 wins
	winnerSum = sum([((i+1)*j) for i,j in enumerate(p2[::-1])])
else: # player 1 wins
	winnerSum = sum([((i+1)*j) for i,j in enumerate(p1[::-1])])
print(winnerSum)
