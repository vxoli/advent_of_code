# AoC 2021 d05

def read_data(filename):
	with open(filename) as file:
		data = [line.strip('\n') for line in list(file)]
	file.close()
	return data

def part1(coordinates):

	# 1. need to determine size of grid and define 2D array [max-x,max-y] to form map. set all to 0
	# 2. loop through coordinates and if x1 == x2 or y1 == y2 then plot on map by incrementing each location
	# 3. count number locations greater than 1

	# 1. need to determine size of grid and define 2D array [max-x,max-y] to form map. set all to 0
	max_x = 0
	max_y = 0
	for line in coordinates:
		x1 = int(line.split(' -> ')[0].split(',')[0])
		y1 = int(line.split(' -> ')[0].split(',')[1])
		x2 = int(line.split(' -> ')[1].split(',')[0])
		y2 = int(line.split(' -> ')[1].split(',')[1])
		
		max_x = (max_x < x1) * x1 + (max_x >= x1) * max_x
		max_x = (max_x < x2) * x2 + (max_x >= x2) * max_x
		max_y = (max_y < y1) * y1 + (max_y >= y1) * max_y
		max_y = (max_y < y2) * y2 + (max_y >= y2) * max_y

	map = [[0]* (((max_x>=max_y)*max_x + (max_x < max_y)*max_y)+1)  for i in range( (((max_x>=max_y)*max_x + (max_x < max_y)*max_y))+1 )]

# 2. loop through coordinates and if x1 == x2 or y1 == y2 then plot on map by incrementing each location
	for line in coordinates:
		x1 = int(line.split(' -> ')[0].split(',')[0])
		y1 = int(line.split(' -> ')[0].split(',')[1])
		x2 = int(line.split(' -> ')[1].split(',')[0])
		y2 = int(line.split(' -> ')[1].split(',')[1])
		if x1 == x2: # horizontal line
			if y1 > y2: y1,y2 = y2,y1
			for y in range(y1,y2+1):
				map[x1][y] += 1
		elif y1 == y2: # vertical line
			if x1 > x2: x1,x2 = x2,x1
			for x in range(x1,x2+1):
				map[x][y1] += 1

# 3. count number locations greater than 1
	counter = 0
	total = 0
	for row in map:
		counter = sum(i>=2 for i in row)
		total += counter

	return total

def part2(coordinates):
# first part follow part1()
# 1. need to determine size of grid and define 2D array [max-x,max-y] to form map. set all to 0
	max_x = 0
	max_y = 0
	for line in coordinates:
		x1 = int(line.split(' -> ')[0].split(',')[0])
		y1 = int(line.split(' -> ')[0].split(',')[1])
		x2 = int(line.split(' -> ')[1].split(',')[0])
		y2 = int(line.split(' -> ')[1].split(',')[1])
		
		max_x = (max_x < x1) * x1 + (max_x >= x1) * max_x
		max_x = (max_x < x2) * x2 + (max_x >= x2) * max_x
		max_y = (max_y < y1) * y1 + (max_y >= y1) * max_y
		max_y = (max_y < y2) * y2 + (max_y >= y2) * max_y

	map = [[0]* (((max_x>=max_y)*max_x + (max_x < max_y)*max_y)+1)  for i in range( (((max_x>=max_y)*max_x + (max_x < max_y)*max_y))+1 )]

# 2. loop through coordinates and if x1 == x2 or y1 == y2 then plot on map by incrementing each location
	for line in coordinates:
		x1 = int(line.split(' -> ')[0].split(',')[0])
		y1 = int(line.split(' -> ')[0].split(',')[1])
		x2 = int(line.split(' -> ')[1].split(',')[0])
		y2 = int(line.split(' -> ')[1].split(',')[1])
		if x1 == x2: # horizontal line
			print('HORIZONTAL')
			for y in range(y1,y2+1):
				map[x1][y] += 1
		elif y1 == y2: # vertical line
			print('VERTICAL')
			if x1 > x2: x1,x2 = x2,x1
			for x in range(x1,x2+1):
				map[x][y1] += 1
# 3. loop through diagonals
		else:
			x = x1
			y = y1
			if x1 < x2 and y1 < y2: 
				print('DIAGONAL top Left to bottom Right')
				while x <= x2 and y <= y2:
					map[x][y] += 1
					x += 1
					y += 1
			if x1 < x2 and y1 > y2:
				print('DIAGONAL top right to bottom left')
				while x <= x2 and y >= y2:
					map[x][y] += 1
					x += 1
					y += -1
			if x1 > x2 and y1 < y2:
				print('DIAGONAL bottom left to top right')
				while x >= x2 and y <= y2:
					map[x][y] += 1
					x += -1
					y += 1
			if x1 > x2 and y1 > y2: 
				print('DIAGONAL bottom right to top left')
				while x >= x2 and y >= y2:
					map[x][y] += 1
					x += -1
					y += -1

# 4. count number locations greater than 1
	counter = 0
	total = 0
	for row in map:
		counter = sum(i>=2 for i in row)
		total += counter

	return total

# start main block
input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d05-input.txt')
print("Part 1: At how many points do at least two lines overlap? ", part1(input_data))
print(part2(input_data))