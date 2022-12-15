# AoC 2022
# --- Day 14: Regolith Reservoir---

import urllib.request

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	
	return data

def find_min_max(data, posn): #posn = 0 or 1
	max = 0
	min = 100000
	for line in data:
		co_ordinates = line.split('->')
		for x in co_ordinates:
			if int(x.split(',')[posn]) > max: max = int(x.split(',')[posn])
			if int(x.split(',')[posn]) < min: min = int(x.split(',')[posn])

	return (min,max)

def make_grid(data):
	max_x = find_min_max(data,0)[1]
	min_x = find_min_max(data,0)[0]
	max_y = find_min_max(data,1)[1]
	min_y = 0 #find_min_max(data,1)[0]
	air = '.'
	rock = "#"
	source = "+"
	grid = [[air for y in range(max_y-min_y+1)] for x in range(max_y-min_y+1)]
	for line in data:
		co_ords = line.split('->')
		for i, pair in enumerate(co_ords[:-1]):
			start_x = int(pair.split(',')[0])
			start_y = int(pair.split(',')[1])
			end_x = int(co_ords[i+1].split(',')[0])
			end_y = int(co_ords[i+1].split(',')[1])
			if start_x == end_x:
				for y in range(min(start_y,end_y),max(start_y,end_y)+1):
					grid[y-min_y][start_x-min_x] = rock
					
			if start_y == end_y: 
				for x in range(min(start_x,end_x),max(start_x, end_x)+1):
					grid[start_y-min_y][x-min_x] = rock

	grid[0-min_y][500-min_x]=source
	return [grid, min_x, max_x, min_y, max_y]

def drop_sand(grid, min_x, max_x, min_y, max_y, full):
	air = '.'
	rock = "#"
	source = "+"
	sand = "o"
	start_x, start_y = 500,0
	x = 500
	y = 0
	try:
		while grid[y][x-min_x] != rock and grid[y][x-min_x] != sand:
			y += 1
		y -= 1
		grid[y][x-min_x] = sand
		can_fall = True
		while can_fall:
			if grid[y+1][x-min_x] == air:
				grid[y][x-min_x] = air
				grid[y+1][x-min_x] = sand
				y += 1
			elif grid[y+1][x-min_x-1] == air:
				grid[y][x-min_x] = air
				grid[y+1][x-min_x-1] = sand
				y += 1
				x -= 1
			elif grid[y+1][x-min_x+1] == air:
				grid[y][x-min_x] = air
				grid[y+1][x-min_x+1] = sand
				y += 1
				x += 1
			else: can_fall = False
	except: 
		full = True
		return [grid, min_x, max_x, min_y, max_y, full]

	return [grid, min_x, max_x, min_y, max_y, full]


def part_1(data):
	grid, min_x, max_x, min_y, max_y = make_grid(data)
	sand_units = 0
	full = False
	while full == False:
		sand_units += 1
		grid, min_x, max_x, min_y, max_y, full = drop_sand(grid, min_x, max_x, min_y, max_y, full)
	return grid, sand_units-1

# input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d14-input.txt')
input = ['498,4 -> 498,6 -> 496,6','503,4 -> 502,4 -> 502,9 -> 494,9']
grid, sand_units = part_1(input)

for line in grid: print(line)
print(sand_units)