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
player1_start, player2_start = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d21-input.txt')
# Test Data
player1_pos = 4
player2_pos = 8
player1_score = 0
player2_score = 0
dice = 1
while player1_score < 1000 and player2_score < 1000:
	player1_pos += dice + dice + 1 + dice + 2 #(3*dice + 3)
	if player1_pos > 10: player1_pos = player1_pos % 10
	player1_score += player1_pos
	dice += 3
#	if dice > 100: dice -= 100
	print(player1_pos, "---", player2_pos, "---", dice)
	player2_pos += dice + dice + 1 + dice + 2
	if player2_pos > 10: player2_pos = player2_pos % 10
	player2_score += player2_pos
	dice += 3
#	if dice > 100: dice -= 100
	print(player1_pos, "---", player1_score, "---", player2_pos, "---",player2_score, "---", dice)

print(player1_score, "---", player2_score)
