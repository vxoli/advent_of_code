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
			data.append(line.strip())

	return data

def part_1(data):
	# lets work with a dictionary with {key: position in sequence, and value the number}.
	moves = data.copy()
	for move in moves: 
	#remove each number from current position (cp) and reinsert into new position (np)
		if move == 0: continue
		cp = data.index(move)
		if move <0: move=move-1
		if cp+move > len(data): move = move + 1
		np = (cp+move)%(len(data))
		temp = data[cp]
		data= data[:cp]+data[cp+1:]
		data = data[:np] + [temp] + data[np:]
	sum = 0
	for i in (1000,2000,3000):
		sum += data[(data.index(0)+(i%len(data)))%len(data)]

	return sum

# def make_dict(data):
# 	data_dict = {}
# 	for i,line in enumerate(input):
# 		data_dict[i]=line
# 	return data_dict

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d20-input.txt')
#input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d20-input.txt")
input = [1,2,-3,3,-2,0,4]
print(part_1(input))



# move by retrieving number, calulating new position, moving other items up amd storing new position