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

# MAIN
grid_data, fold_data = read_url()
## TEST DATA
grid_data = ['6,10','0,14','9,10','0,3','10,4','4,11','6,0','6,12','4,1','0,13','10,12','3,4','3,0','8,4','1,10','2,14','8,10','9,0']
fold_data = ["old along y=7","fold along x=5"]
## END TEST DATA
grid = generate_grid(grid_data)
print(grid)