# AoC 2022
# --- Day 18: Boiling Boulders ---

import urllib.request
import numpy as np

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def parse(data):
	output = set()
	for line in data:
		x,y,z = map(int, line.split(","))
		output.add((x,y,z))
	return output

def part_1(data):
	uncovered_sides = 0
	for x,y,z in data:
		covered_sides = 0
		pos = np.array((x,y,z))
		for coord in range(3):
			deltapos = np.array([0,0,0])
			deltapos[coord] = 1

			deltaneg = np.array([0,0,0])
			deltaneg[coord] = -1

			covered_sides += tuple(pos+deltapos) in data
			covered_sides += tuple(pos+deltaneg) in data

		uncovered_sides += 6 - covered_sides

	return uncovered_sides

input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d18-input.txt')
#input = [[2,2,2],[1,2,2],[3,2,2],[2,1,2],[2,3,2],[2,2,1],[2,2,3],[2,2,4],[2,2,6],[1,2,5],[3,2,5],[2,1,5],[2,3,5]]
#input = [[1,1,1],[2,1,1]]
input = parse(input) # converts to set of x,y,z
print(part_1(input))