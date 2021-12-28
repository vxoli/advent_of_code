# AoC 2021 D21
# --- Day 21: Dirac Dice ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")

	return (int(data[0][28:]), int(data[1][28:]))

# Main
player1_pos, player2_pos = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d21-input.txt')
player1_score = 0
player2_score = 0
dice = 1
rolls = 0
while player1_score < 1000 and player2_score < 1000:
	for _ in range(3):
		player1_pos += dice % 10
		if player1_pos > 10: player1_pos = player1_pos % 10
		dice = ((dice) % 100) + 1
		rolls += 1
	player1_score += player1_pos
	if player1_score >= 1000: break
	for _ in range(3):
		player2_pos += dice % 10
		if player2_pos > 10: player2_pos = player2_pos % 10
		dice = ((dice) % 100) + 1
		rolls += 1
	player2_score += player2_pos
	if player2_score >= 1000: break

losing_score = (player1_score>player2_score)* player2_score + (player2_score>player1_score)* player1_score
print("Part 1: ",rolls, "rolls * loser score = ",rolls * losing_score)