# AoC 2021 d25
# --- Day 25: Sea Cucumber ---

import urllib.request
import copy

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
#	data = data.split("\n")
	data = [list(line) for line in data.split("\n")]

	return data

def move(grid, indicator):
	new_grid = copy.deepcopy(grid)
	any_moved = False
	for row in range(rows):
		for col in range(cols):
			if indicator != grid[row][col]:
				continue
			if grid[row][col] == "v":
				dest = (row+1)%rows, col
			else:
				dest = row,(col+1)%cols

			if grid[dest[0]][dest[1]] == ".":
				any_moved = True
				new_grid[dest[0]][dest[1]] = grid[row][col]
				new_grid[row][col] = "."

	return new_grid, any_moved

# Main
map = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d25-input.txt')

rows = len(map)
cols = len(map[0])

steps = 0

while True:
	map, any_moved_e = move(map, ">")
	map, any_moved_s = move(map, "v")
	steps += 1
	if not(any_moved_e or any_moved_s): break

print("Part 1: What is the first step on which no sea cucumbers move?: ",steps) 