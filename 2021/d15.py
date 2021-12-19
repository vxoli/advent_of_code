# Aoc 2021 d15
# --- Day 15: Chiton ---
import urllib.request
import heapq

def read_url(url):
	file = urllib.request.urlopen(url)
	data = file.read().strip()
	data = data.decode("utf8")
	#data = data.split("\n")
	# # test data
	# data = ['1163751742','1381373672','2136511328','3694931569','7463417111','1319128137','1359912421','3125421639','1293138521','2311944581']
	data = [[int(i) for i in line] for line in data.split("\n")] #add .split("\n") for real data
	
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

# Main
map_data = read_url('https://raw.githubusercontent.com/vxoli/adventofcode/main/2021/d15-input.txt')
risk = navigate(map_data)
print(risk)