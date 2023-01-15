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

def swap(nums, a, b):
	nums[a],nums[b]=nums[b],nums[a]
	return nums

def part_1(code):
	moves = code.copy()
	moves = [[int(i),'.'] for i in moves]
	n = len(moves)
	while len([i[1] for i in moves if i[1] == '.']) > 0:
		posn = 0
		while moves[posn][1] == 'x':
			posn += 1
		move = moves[posn]
		num_to_move = move[0]
#		if num_to_move == 0: continue
		move_from = moves.index([move[0],'.'])
		moves[posn] = [num_to_move,'x']
		move_to = (move_from + num_to_move) % n
		difference = (move_to - move_from)%n
		if num_to_move < 0: difference = (difference + n -1) % n
		for i in range(difference):
			moves = swap(moves,(i+posn)%n,(i+posn+1)%n)
		if move_to-move_from<0 and num_to_move>0:
			moves = [moves[n-1]] + moves[:n-1]

	index = moves.index([0,'x'])
	sum = 0
	for i in (1000,2000,3000):
		print(int((moves[((i+index)%(len(moves)))][0])))
		sum += int((moves[((i+index)%(len(moves)))][0]))

	return sum

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d20-input.txt')
#input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d20-input.txt")
#input = ['1','2','-3','3','-2','0','4'] # Test data
print("What is the sum of the three numbers that form the grove coordinates?",part_1(input))
