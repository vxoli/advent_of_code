def read_data(filename):
	with open(filename) as file:
		data = [x for x in file.read().split('\n')]
	return data

def part1(heightmap):
	risklevel = 0
	heightmap = ['2199943210','3987894921','9856789892','8767896789','9899965678']
	for line_index,line in enumerate(heightmap):
		for char_index,char in enumerate(line):
			height = int(char)

			offset_x = (-1,+1)
			offset_y = (-1,+1)

			if line_index -1 < 0:
				offset_y = (0,+1)
			if line_index + 1 >= len(heightmap)-1:
				offset_y = (0,-1)
			if char_index -1 < 0:
				offset_x = (+1,0)
			if char_index + 1 >= len(line)-1:
				offset_x = (-1,0)

			print(line_index,"---",offset_y,"---",offset_x)
			height = int(char)
			height_up = int(heightmap[line_index+offset_y[0]][char_index])
			height_down = int(heightmap[line_index+offset_y[1]][char_index])
			height_left = int(heightmap[line_index][char_index+offset_x[0]])
			height_right = int(heightmap[line_index][char_index+offset_x[1]])

			if height < height_up and height < height_down and height < height_left and height < height_right:
				print(height)
				risklevel += height + 1

	return risklevel


# main
input_data = read_data('/home/christopher/Documents/GitHub/adventofcode/2021/d09-input.txt')
print(part1(input_data))