# AoC 2021 d25
# --- Day 25: Sea Cucumber ---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")

	return data

map = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d25-input.txt')

moved = True
steps = 0
while moved:
	moved=False
	new_map = [[[]for _ in range(len(map[0]))] for _ in range(len(map))]
	for i,line in enumerate(map):
		for j,char in enumerate(line):

			if char == ".": 
				new_map[i][j] = "."
				continue

			if char == ">":
				if map[i][((j+1)%(len(line)))] != ".":
					new_map[i][j] = ">"
					continue
				else:
					new_map[i][j]="."
					new_map[i][((j+1)%(len(line)))]=">"
					moved=True
					continue

			if char == "v":
				if map [((i+1)%(len(map)))][j] != ".":
					new_map[i][j] = "v"
					continue
				else:
					new_map[i][j] = "."
					new_map[((i+1)%(len(map)))][j] = 'v'
					moved=True
					continue
	steps += 1
	map = new_map
