# AoC 2022
# --- Day 20: Grove Positioning System ---

import urllib.request

def read_url(url): #read from github file
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def read_file(filename): # read from disk
	data = []
	with open(filename) as f:
		for line in f:
			data.append(int(line.strip()))

	return data

def part_1(code):
	moves = [[int(i),'.'] for i in code]
	while len([i[1] for i in moves if i[1] == '.']) > 0:
		posn = 0
		while moves[posn][1] == 'x': 
			posn += 1
		move = moves[posn]
		num_to_move = move[0]
		move_from = moves.index([move[0],'.'])
		if num_to_move < 0: 
			move_to = (((num_to_move + move_from) % len(moves)) -1) % len(moves)
			first_part = moves[:move_from]
			mid_part = moves[move_from+1:move_to+1]
			end_part = moves[move_to+1:]
			moves = first_part + mid_part + [[str(num_to_move),'x']] + end_part

		elif num_to_move + move_from > len(moves): 
			move_to = (((num_to_move + move_from) % len(moves)) +1) % len(moves)
			first_part = moves[:move_to]
			mid_part = moves[move_to:move_from]
			end_part = moves[move_from+1:]
			moves = first_part + [[str(num_to_move),'x']] + mid_part + end_part

		else:
			move_to = (num_to_move + move_from) % len(moves)
			first_part = moves[:move_from]
			mid_part = moves[move_from+1:move_to+1]
			end_part = moves[move_to+1:]
			moves = first_part + mid_part + [[str(num_to_move),'x']] + end_part

	moves = [i[0]  for i in moves]
	print(moves)
	sum = 0
	print(moves.index('0'))
	for i in (1000,2000,3000):
		print(int((moves[(i+moves.index('0'))%(len(moves))])))
		sum += int((moves[(i+moves.index('0'))%(len(moves))]))

	return sum

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d20-input.txt')
#input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d20-input.txt")
input = ['1','2','-3','3','-2','0','4'] # Test data
print("What is the sum of the three numbers that form the grove coordinates?",part_1(input))



# move by retrieving number, calulating new position, moving other items up amd storing new position