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
	print(max_x,',',min_x,',',max_y,',',min_y)
	grid = [['.' for y in range(max_y-min_y+1)] for x in range(max_y-min_y+1)]
	for line in grid: print(line)
	for line in data:
		co_ords = line.split('->')
		for i, pair in enumerate(co_ords[:-1]):
			start_x = int(pair.split(',')[0])
			start_y = int(pair.split(',')[1])
			end_x = int(co_ords[i+1].split(',')[0])
			end_y = int(co_ords[i+1].split(',')[1])
			print(start_x,',',start_y,'--',end_x,',',end_y)
			if start_x == end_x:
				for y in range(min(start_y,end_y),max(start_y,end_y)+1):
					print(y)
					print(grid[max_x-start_x-1][y])
					grid[y-min_y][start_x-min_x] ='#'
					for line in grid: print(line)
					
			if start_y == end_y: 
				for x in range(min(start_x,end_x),max(start_x, end_x)+1):
					print(x,min(start_x,end_x),max(start_x,end_x)+1)
					print(x,min_x,max_x,x-min_x)
					grid[start_y-min_y][x-min_x] ='#'
					for line in grid: print(line)


		# for x in co_ords:
		# 	print(x)


	return grid

def part_1(data):

	return

# input = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2022/d14-input.txt')
input = ['498,4 -> 498,6 -> 496,6','503,4 -> 502,4 -> 502,9 -> 494,9']
grid = make_grid(input)
for line in grid: print(line)