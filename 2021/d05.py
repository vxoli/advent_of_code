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

	map = [[0]* max_x for i in range(max_y) ]

# 2. loop through coordinates and if x1 == x2 or y1 == y2 then plot on map by incrementing each location

	return

input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d05-input.txt')
print(input_data[1].split(' -> '))
part1(input_data)