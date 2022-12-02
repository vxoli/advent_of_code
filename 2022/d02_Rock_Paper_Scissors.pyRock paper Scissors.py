# D02 AoC 2022 Rock paper Scissors

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def part_1(plays):
    score = 0
    for play in plays:
        elf_play = play.split()[0]
        # A = Rock B = Paper C = Scissors
        my_play = play.split()[1]
        # X = Rock Y = Paper Z = Scissors

        if elf_play == 'A':
            if my_play == 'X':
                result = "tie"
            if my_play == 'Y':
                result = "win"
            if my_play == 'Z':
                result = "lose"
        if elf_play == 'B':
            if my_play == 'X':
                result = "lose"
            if my_play == "Y":
                result = "tie"
            if my_play == "Z":
                result = "win"
        if elf_play == "C":
            if my_play == 'X':
                result = "win"
            if my_play == "Y":
                result = "lose"
            if my_play == "Z":
                result = "tie"

        if result == "win":
            score += 6 + (my_play == "X") * 1 + (my_play == "Y") * 2 + (my_play == 'Z') * 3
        if result == "tie":
            score += 3 + (my_play == "X") * 1 + (my_play == "Y") * 2 + (my_play == 'Z') * 3
        if result == "lose":
            score += (my_play == "X") * 1 + (my_play == "Y") * 2 + (my_play == 'Z') * 3

    return score

def Part_2(plays):

    return

input_data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d02-input.txt')
print("Part 1: What would your total score be if everything goes exactly according to your strategy guide?", part_1(input_data))
