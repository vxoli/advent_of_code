def read_data(filename):
	with open(filename) as file:
		data = [x for x in file.read().split('\n')]
	return data

def part1(heightmap):
#	heightmap = ['2199943210','3987894921','9856789892','8767896789','9899965678']

## try this - what ive been trying to do...
	rows = len(heightmap)-1
	cols = len(heightmap[0])

	risklevel = 0
	# Find low points
	for row in range(rows):
	    for col in range(cols):
	        lowpoint = True
	        for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
	            rr = row + d[0]
	            cc = col + d[1]

	            if not ((0 <= rr and rr < rows) and (0 <= cc and cc < cols)):
	                continue

	            if int(heightmap[rr][cc]) <= int(heightmap[row][col]):
	                lowpoint = False
	                break

	        if lowpoint:
	            risklevel += int(heightmap[row][col]) + 1



	return risklevel


# main
input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d09-input.txt')
print(part1(input_data))