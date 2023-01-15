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

def part_1(moves):
	code = moves.copy()
	n = len(code)
	for move in moves:
		posn = code.index(move)
		move_to = (posn + move) % n
		difference = (move_to - posn) % n
		if move < 0: difference = (difference + n -1) % n
		for i in range(difference):
			code = swap(code,(i+posn)%n,(i+posn+1)%n)
		if move_to-posn<0 and move > 0:
			code = [code[n-1]] + code[:n-1]
	
	index = code.index(0)
	sum = 0
	for i in (1000,2000,3000):
		sum += int((code[((i+index)%(len(code)))]))

	return sum

def part_2(moves):
	code = moves.copy()
#	code  = [[int(i),'.'] for i in code]
	n = len(code)
	for move in moves:
		posn = code.index(move)
		move_to = (posn + move) % n
		difference = (move_to - posn) % n
		if move < 0: difference = (difference + n -1) % n
		# print(code)
		# print(move)
		# print(posn, move_to, difference)
		for i in range(difference):
			code = swap(code,(i+posn)%n,(i+posn+1)%n)
		if move_to-posn<0 and move > 0:
			code = [code[n-1]] + code[:n-1]
	index = code.index(0)


	# sum = 0
	# for i in (1000,2000,3000):
	# 	sum += int((code[((i+index)%(len(code)))]))

	return sum


#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d20-input.txt')
#input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d20-input.txt")
input = ['1','2','-3','3','-2','0','4'] # Test data
input = [int(i) for i in input]
print("Part 1: What is the sum of the three numbers that form the grove coordinates?",part_1(input))

#print(part_2([int(i) for i in input]))
