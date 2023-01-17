# AoC 2022
# --- Day 23: Unstable Diffusion ---
from collections import defaultdict
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

grid = read_file("/home/christopher-spectre/Development/advent_of_code/2022/d23-input.txt")

#grid = ['....#..','..###.#','#...#.#','.#...##','#.###..','##.#.##','.#..#..']
#grid = ['..............','..............','.......#......','.....###.#....','...#...#.#....','....#...##....','...#.###......','...##.#.##....','....#..#......','..............','..............','..............']


checks = [
	[[1,2,3],2],
	[[7,6,5],6],
	[[5,4,3],4],
	[[1,0,7],0]]

n = len(grid)
m = len(grid[0])

elves = set()

for i in range(n):
	for j in range(m):
		if grid[i][j] == '#':
			elves.add((i,j))

dirs = [
	[ 0, 1],
	[-1, 1],
	[-1, 0],
	[-1,-1],
	[ 0,-1],
	[ 1,-1],
	[ 1, 0],
	[ 1, 1]]

def get_bounds(elves):
	min_row = 1 << 60
	max_row = -(1 << 60)
	min_col = 1 << 60
	max_col = -(1 << 60)

	for row, col in elves:
		min_row = min(min_row, row)
		max_row = max(max_row, row)
		min_col = min(min_col, col)
		max_col = max(max_col, col)

	return min_row, max_row, min_col, max_col

def print_elves(elves):
	min_row, max_row, min_col, max_col = get_bounds(elves)
	for row in range(min_row, max_row+1):
		for col in range(min_col, max_col+1):
			if (row, col) in elves:
				print('#', end="")
			else:
				print('.', end="")
		print()

for round in range(10):
	propose = {}
	proposed = defaultdict(int)
	for elf in elves:
		row, col = elf

		good = False
		for drow, dcol in dirs:
			if (row + drow, col+dcol) in elves:
				good = True
				break
		if not good:
			continue

		for check_dirs, propose_dir in checks:
			good = True
			for d in check_dirs:
				drow, dcol = dirs[d]
				if (row + drow, col+dcol) in elves:
					good = False
					break
			if not good:
				continue

			drow, dcol = dirs[propose_dir]
			propose[elf] = (row + drow, col + dcol)
			proposed[propose[elf]] += 1
			break

	new_elves = set()
	for elf in elves:
		if elf in propose:
			new_loc = propose[elf]
			if proposed[new_loc] > 1 or proposed[new_loc] == 0:
				new_elves.add(elf)
			else:
				new_elves.add(new_loc)
		else:
			new_elves.add(elf)

	checks = checks[:1] + [checks[0]]
	elves = new_elves

min_row, max_row, min_col, max_col = get_bounds(elves)
print(min_row,max_row)
print(max_row,max_col)
print((max_row - min_row + 1) * (max_col - min_col + 1) - len(elves))

