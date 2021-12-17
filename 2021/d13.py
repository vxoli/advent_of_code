# AoC 2021 d13
# --- Day 13: Transparent Origami ---

import urllib.request

def read_url():
	file = urllib.request.urlopen('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d13-input.txt')
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	folds = [x for x in data if x[:4] == "fold"]
	coordinates = data[:len(data)-len(folds)-1]

	return coordinates,folds

def generate_grid(coordinates):
	
	max_x = max(list([int(x.split(",")[0]) for x in coordinates]))
	max_y = max(list([int(y.split(",")[1]) for y in coordinates]))
	grid = [["." for _ in range(max_x+1)] for _ in range(max_y+1)]
	for location in coordinates:
		x = int(location.split(",")[0])
		y = int(location.split(",")[1])
		grid[y][x] = "#"

	return grid

def fold_grid(fold_instruction, grid):
	# split off "fold along "
	fold_axis = fold_instruction[11:].split('=')[0]
	fold_index = int(fold_instruction[11:].split('=')[1])

	if fold_axis == 'y':
		grid = fold_y(fold_index, grid)
	if fold_axis == 'x':
		grid = fold_x(fold_index, grid)


	return grid

def fold_y(fold_index, grid):
	# y represents a horizontal line
	# Because this is a horizontal line, fold the bottom half up. Some of the 
	# dots might end up overlapping after the fold is complete, but dots will 
	# never appear exactly on a fold line.

	lines_below = len(grid) - fold_index - 1
	for row in range(lines_below):
		for col in range(len(grid[row])):
			if grid[fold_index + row + 1][col] == "#":
				grid[fold_index - row -1][col] = "#"

	grid = grid[:fold_index] # drop folded lines off bottom of grid
	return grid

def fold_x(fold_index, grid):
	#Because this is a vertical line, fold left:
	lines_right = len(grid[0])-fold_index - 1

	for row in range(len(grid)):
		for col in range(lines_right):
			if grid[row][fold_index+col+1] == '#':
				grid[row][fold_index-col-1] = "#"

	# # drop folded rows off from right of grid
	grid = [row[:fold_index] for row in grid]
	
	
	return grid

def count_dots(grid):
	total_dots = 0
	for row in grid:
		total_dots += row.count("#")

	return total_dots


# MAIN
grid_data, fold_data = read_url()
# ## TEST DATA
# grid_data = ['6,10','0,14','9,10','0,3','10,4','4,11','6,0','6,12','4,1','0,13','10,12','3,4','3,0','8,4','1,10','2,14','8,10','9,0']
# fold_data = ["fold along y=7","fold along x=5"]
# ## END TEST DATA

# Part 1
grid = generate_grid(grid_data)
grid = fold_grid(fold_data[0], grid)
print("Part 1: How many dots are visible after completing just the first fold instruction on your transparent paper? ",count_dots(grid))

# Part 2

grid_data, fold_data = read_url()
grid = generate_grid(grid_data)
for fold in fold_data:
	grid = fold_grid(fold, grid)
print("Part 2: What code do you use to activate the infrared thermal imaging camera system?")
for row in grid:
	for char in row:
		print(char, end="")
	print("")
