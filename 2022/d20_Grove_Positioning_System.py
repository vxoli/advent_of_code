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

#input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d20-input.txt')
#input = [1,2,-3,3,-2,0,4]
input = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d20-input.txt")

for line in input: print(line)
