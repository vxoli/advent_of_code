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
		cp = data.index(move)
		print(data)
		np = (cp + move)%len(data)
		list_before = data[:cp]
		list_after = data[(cp+1)%len(data):]
		temp = data[cp]
		print(cp,np,temp)
		print(list(list_before+[temp]+list_after))
		num_move = list_after[cp:np]
		list_remain = list_after[np:]
		print(num_move, list_remain)
		print(list(list_before+num_move+[temp]+list_remain))
		data = list(list_before+num_move+[temp]+list_remain)



	return

# def make_dict(data):
# 	data_dict = {}
# 	for i,line in enumerate(input):
# 		data_dict[i]=line
# 	return data_dict

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d20-input.txt')
#input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d20-input.txt")
input = [1,2,-3,3,-2,0,4]
part_1(input)



# move by retrieving number, calulating new position, moving other items up amd storing new position