# Aoc 2021 d15
# --- Day 15: Chiton ---
import urllib.request
import heapq

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	data = data.split("\n")
	# # test data
	# data = ['1163751742','1381373672','2136511328','3694931569','7463417111','1319128137','1359912421','3125421639','1293138521','2311944581']
	data = [[int(i) for i in line] for line in data] #add .split("\n") for real data
	
	return data

def navigate(map):
	y_length = len(map)
	x_length = len(map[0])
	risk = dict()
	pq=[(0,0,0)]
	heapq.heapify(pq)
	visited = set()

	while len(pq) > 0:
		c , row, col = heapq.heappop(pq)

		if (row, col) in visited:
			continue
		visited.add((row,col))

		risk[(row,col)] = c

		if row == y_length-1 and col == x_length-1:
			break

		for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
			rr = row + dr
			cc = col + dc
			if not(0 <= rr < y_length and 0 <= cc < x_length):
				continue
			heapq.heappush(pq, (c+map[rr][cc], rr, cc))

	return risk[(y_length-1, x_length-1)]

def generate_new_map(map):
	#generates new grid
	#The entire cave is actually five times larger in both dimensions than you thought; the area you originally 
	#scanned is just one tile in a 5x5 tile area that forms the full map. Your original map tile repeats to the 
	#right and downward; each time the tile repeats to the right or downward, all of its risk levels are 1 higher 
	#than the tile immediately up or left of it. However, risk levels above 9 wrap back around to 1.

	rows = len(map)
	cols = len(map[0])
	newmap = [[0 for row in range(rows*5)] for col in range(cols * 5)]
	# add 4 grids to the right of original
	for i in range(5):
		for x in range(rows):
			for y in range(cols):
				newmap[x][y+(i*cols)] = (map[x][y]+(1*i))
				if newmap[x][y+(i*cols)] > 9: newmap[x][y+(i*cols)] -= 9
	# add 4 grids below the new grid
	cols = len(newmap[0])
	for i in range(5):
		for x in range(rows):
			for y in range(cols):
				newmap[x+(i*rows)][y] = newmap[x][y]+(1*i)
				if newmap[x+(i*rows)][y] > 9: newmap[x+(i*rows)][y] -= 9

	return newmap

# Main
map_data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d15-input.txt')
print("Part 1: What is the lowest total risk of any path from the top left to the bottom right? ",navigate(map_data))
print("Part 2: Using the full map, what is the lowest total risk of any path from the top left to the bottom right? ", navigate(generate_new_map(map_data)))